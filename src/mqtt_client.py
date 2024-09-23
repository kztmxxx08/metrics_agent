import os

import paho.mqtt.client as mqtt
from dotenv import load_dotenv

from .logger_record import metrics_logging_handler, error_logging_handler


class MQTTClient:
    def __init__(self):
        load_dotenv()
        self.mqtt_broker = os.getenv('MQTT_BROKER')
        self.mqtt_port = int(os.getenv('MQTT_PORT'))

        self.client = mqtt.Client()
        # self.configure_client()
        self.connected = False

    def configure_client(self):
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_publish = self.on_publish

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            metrics_logging_handler(
                "connect status", "INFO",
                "MQTT on connect"
            )
        else:
            error_logging_handler(
                "connect status", "ERROR",
                f"Failed to connect, return code is {rc}"
            )

    def on_disconnect(self, client, userdata, rc):
        metrics_logging_handler(
            "disconnect status", "INFO",
            f"Disconnect from MQTT Broker, return code is {rc}"
        )

    def on_publish(self, client, userdata, mid):
        metrics_logging_handler(
            "publish status", "INFO",
            f"Message published. "
        )

    def connect(self):
        try:
            self.client.connect(host=self.mqtt_broker, port=self.mqtt_port)  # 固定ブローカーに接続
            self.connected = True
            self.client.loop_start()
        except Exception as e:
            error_logging_handler(
                "MQTT connect", "ERROR",
                f"Connection failed: {e}"
            )

    def is_connected(self):
        return self.connected

    def publish(self, topic, message):
        try:
            result = self.client.publish(topic, message)
            if result[0] == 0:
                metrics_logging_handler(
                    f"{topic} metrics", "INFO",
                    message
                )
            else:
                error_logging_handler(
                    f"{topic} metrics", "ERROR",
                    f"Failed to publish message to topic {topic}: rc is {result[0]}"
                )
        except Exception as e:
            error_logging_handler(
                f"MQTTPublish", "ERROR",
                f"Failed to publish message: {e}"
            )
            raise

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()