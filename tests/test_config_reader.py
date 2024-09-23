import pytest

from src.load_config import ConfigReader


class TestConfigReader:
    def test_load_config_info(self):
        loader = ConfigReader()
        assert isinstance(loader.load_config_info(), dict)

    def test_load_logging_info(self):
        loader = ConfigReader()
        assert isinstance(loader.load_config_logging_info(), dict)