import os
import time

import psutil

from . import load_config
from .mqtt_client import MQTTClient

from .logger_record import metrics_logging_handler, error_logging_handler


class SystemMetrics:
    def __init__(self):
        self.host_name = os.uname().nodename.replace(".local", "")
        self.config = load_config.ConfigReader().load_config_info()["metrics"]
        self.metrics_interval = self.config["metrics_interval"]
        self.cpu_interval = self.config["cpu_interval"]

        self.cpu_usage = list()
        self.memory_usage = 0.0
        self.swap_usage = 0.0
        self.disk_usage = 0.0

        self.mqtt_client = MQTTClient()

    def controller(self):
        try:
            self.mqtt_client.connect()
            while True:
                self._load_system_metrics()
                time.sleep(self.metrics_interval)
        except TypeError as e:
            error_logging_handler(
                "metrics publish", "ERROR",
                f"{e}"
            )
        except AttributeError as e:
            error_logging_handler(
                "metrics publish", "ERROR",
                f"{e}"
            )
        except KeyboardInterrupt as e:
            metrics_logging_handler(
                "KeyboardInterrupt", "INFO",
                f"KeyboardInterrupt"
            )
        finally:
            self.mqtt_client.disconnect()

    def _load_system_metrics(self):
        self.get_cpu_usage()
        self.get_memory_usage()
        self.get_swap_usage()
        self.get_disk_usage()

    def get_cpu_usage(self):
        self.cpu_usage = psutil.cpu_percent(interval=self.cpu_interval, percpu=True)
        topic_name = f"{self.host_name}/CPU"
        cpu_metrics_payload_text = ""
        for index, cpu_metrics in enumerate(self.cpu_usage):
            if len(self.cpu_usage) == index + 1:
                cpu_metrics_payload_text += f"{cpu_metrics}"
            else:
                cpu_metrics_payload_text += f"{cpu_metrics}/"
        self.mqtt_client.publish(topic=topic_name, message=cpu_metrics_payload_text)

    def get_memory_usage(self):
        self.memory_usage = psutil.virtual_memory().percent
        topic_name = f"{self.host_name}/MEMORY"
        self.mqtt_client.publish(topic=topic_name, message=self.memory_usage)

    def get_swap_usage(self):
        self.swap_usage = psutil.swap_memory().percent
        topic_name = f"{self.host_name}/SWAP"
        self.mqtt_client.publish(topic=topic_name, message=self.swap_usage)

    def get_disk_usage(self):
        self.disk_usage = psutil.disk_usage('/').percent
        topic_name = f"{self.host_name}/DIR_ROOT_USAGE"
        self.mqtt_client.publish(topic=topic_name, message=self.disk_usage)
