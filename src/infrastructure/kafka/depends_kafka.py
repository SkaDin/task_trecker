from src.infrastructure.kafka.kafka_produser import KafkaProducer


def kafka_producer_dependency():
    config = {
        "bootstrap.servers": "localhost:29092",
        "client.id": "tasks_service",
    }
    return KafkaProducer(config_producer=config)
