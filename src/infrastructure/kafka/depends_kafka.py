from src.core.config import config as configs
from src.infrastructure.kafka.kafka_produser import KafkaProducer


def kafka_producer_dependency():
    config = {
        "bootstrap.servers": configs.BOOTSTRAP_SERVERS,
        "client.id": configs.CLIENT_ID,
    }
    return KafkaProducer(config_producer=config)
