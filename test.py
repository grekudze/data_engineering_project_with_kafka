# test_import.py
try:
    from six.moves import range
    print("six.moves imported successfully")
except ImportError:
    print("Error importing six.moves")

try:
    from kafka import KafkaProducer
    print("KafkaProducer imported successfully")
except ImportError as e:
    print(f"Error importing KafkaProducer: {e}")
