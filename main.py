from src.logger_record import metrics_logging_handler
from src import system_metrics


def metrics_agent():
    metrics_controller = system_metrics.SystemMetrics()
    metrics_controller.controller()


if __name__ == '__main__':
    metrics_logging_handler("metrics_agent", "INFO",
                            "metrics agent start")
    metrics_agent()
    metrics_logging_handler("metrics_agent", "INFO",
                            "metrics agent end")
