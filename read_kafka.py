from confluent_kafka import Consumer, KafkaException, KafkaError

def read_data():
    # Kafka Consumer конфигурация
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    }

    # Создание Kafka Consumer
    consumer = Consumer(conf)

    # Подписка на топик
    consumer.subscribe(['users-created'])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    raise KafkaException(msg.error())
            # Печать сообщения
            print(f"Received message: {msg.value().decode('utf-8')}")

    except KeyboardInterrupt:
        pass
    finally:
        # Закрытие Consumer
        consumer.close()

if __name__ == "__main__":
    read_data()
