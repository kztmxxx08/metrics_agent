import os

import yaml


class ConfigReader:
    def __init__(self):
        self.config_info_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "config_info.yaml")
        self.config_logging_info_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "config_logging_info.yaml")

    def load_config_info(self):
        with open(self.config_info_path, "r") as config_info_yaml:
            config = yaml.safe_load(config_info_yaml)
            return config

    def load_config_logging_info(self):
        with open(self.config_logging_info_path, "r") as config_logging_info_yaml:
            config = yaml.safe_load(config_logging_info_yaml)
            return config

if __name__ == "__main__":
    config_instance = ConfigReader()
    config_info = config_instance.load_config_info()
    print(config_info)