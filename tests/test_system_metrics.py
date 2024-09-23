import pytest

from src.system_metrics import SystemMetrics

class TestSystemMetrics:
    def setup_method(self):
        self.system_metrics = SystemMetrics()

    def test_get_cpu_usage(self):
        self.system_metrics.get_cpu_usage()
        assert hasattr(self.system_metrics, "cpu_usage")
        assert isinstance(self.system_metrics.cpu_usage, list)
        assert all(isinstance(cpu, float) for cpu in self.system_metrics.cpu_usage)

    def test_get_memory_usage(self):
        self.system_metrics.get_memory_usage()
        assert hasattr(self.system_metrics, "memory_usage")
        assert isinstance(self.system_metrics.memory_usage, float)

    def test_get_swap_usage(self):
        self.system_metrics.get_swap_usage()
        assert hasattr(self.system_metrics, "swap_usage")
        assert isinstance(self.system_metrics.swap_usage, float)

    def test_get_disk_usage(self):
        self.system_metrics.get_disk_usage()
        assert hasattr(self.system_metrics, "disk_usage")
        assert isinstance(self.system_metrics.disk_usage, float)
