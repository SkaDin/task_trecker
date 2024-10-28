import json

from confluent_kafka import Producer


class KafkaProducer:
    def __init__(self, config_producer) -> None:
        self.producer = Producer(config_producer)

    async def send_message(self, topic, message, key=None) -> None:
        message_bytes = json.dumps(message).encode("utf-8")
        self.producer.produce(topic, message_bytes, key=key, callback=KafkaProducer.delivery_report)
        self.producer.flush()

    @classmethod
    def delivery_report(cls, err, msg) -> None:
        if err is not None:
            print(f"Message delivery failed: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")
