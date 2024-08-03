# Проект Data Engineering с использованием Kafka

Этот проект представляет собой комплексный конвейер обработки данных, интегрирующий несколько технологий, включая Apache Kafka, Apache Airflow, PostgreSQL, Apache Spark и Cassandra. Цель проекта - продемонстрировать полный цикл обработки данных, от их получения до обработки и хранения.

## Структура проекта

- **Apache Kafka**: Используется для потоковой передачи данных в реальном времени.
- **Apache Airflow**: Оркестрация рабочего процесса и управление DAGs.
- **PostgreSQL**: Реляционная база данных для хранения структурированных данных.
- **Apache Spark**: Распределенная обработка данных.
- **Cassandra**: NoSQL база данных для обработки данных в крупном масштабе.

## Начало работы

### Требования

- Docker
- Docker Compose
- Git

### Установка

1. **Клонирование репозитория:**

   ```bash
   git clone git@github.com:grekudze/data_engineering_project_with_kafka.git
   cd data_engineering_project_with_kafka
   
Запуск сервисов:

Убедитесь, что Docker запущен на вашем компьютере, затем выполните:
docker compose up -d
Проверка состояния сервисов:
docker ps

Конфигурация
Kafka: Конфигурация для Kafka указана в файле docker-compose.yml.
Airflow: DAGs и другие настройки находятся в директории dags.
PostgreSQL: Учетные данные базы данных настроены в файле docker-compose.yml.
Spark: Конфигурации для мастера и рабочих узлов Spark также указаны в файле docker-compose.yml.
Cassandra: Управление конфигурацией осуществляется в файле docker-compose.yml.

Использование
Доступ к Airflow:

Откройте веб-браузер и перейдите по адресу http://localhost:8080, чтобы получить доступ к веб-интерфейсу Airflow. Используйте учетные данные по умолчанию (если установлены) для входа.

Запуск Kafka Producer:

Kafka producer определен в файле dags/kafka_stream.py. Вы можете запустить его, используя:
python dags/kafka_stream.py

Запуск Kafka Consumer:

Скрипт для Kafka consumer также определен в проекте. Запустите его, используя:
python dags/kafka_consumer.py

Устранение неполадок
Проблемы с Docker: Убедитесь, что Docker установлен и запущен правильно.
Проблемы с Kafka: Проверьте, что Kafka broker и zookeeper находятся в здоровом состоянии.
