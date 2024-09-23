import pytest

from src.mqtt_client import MQTTClient

class TestMQTTClient:
    def test_mqtt_connection(self):
        client = MQTTClient()
        client.connect()
        assert client.is_connected() == True