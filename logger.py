import os
import time
import datetime


class Logger():
    def __init__(self, log_dir, file_name):
        self.log_dir = log_dir
        self.log_full_name = self.init_log_file(self.log_dir, file_name)
        self.metrics = dict()

    def ERROR(self, message, write=True) -> None:
        prefix = "\033[31m"
        suffix = "\033[0m"
        title = "[ERROR]:\t"
        message = title + message
        print(f"{prefix}{message}{suffix}")
        if write:
            self.append_line(message, self.log_full_name)

    def WARNING(self, message, write=True) -> None:
        prefix = "\033[33m"
        suffix = "\033[0m"
        title = "[WARNING]:\t"
        message = title + message
        print(f"{prefix}{message}{suffix}")
        if write:
            self.append_line(message, self.log_full_name)

    def INFO(self, message, write=False) -> None:
        prefix = "\033[32m"
        suffix = "\033[0m"
        title = "[MESSAGE]:\t"
        message = title + message
        print(f"{prefix}{message}{suffix}")
        if write:
            self.append_line(message, self.log_full_name)

    def init_log_file(self, log_dir, file_name) -> str:
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_full_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + "_" + file_name
        log_full_path = os.path.join(log_dir, log_full_name)
        with open(log_full_path, "w") as log_file:
            log_file.write(f"Log File Initialization\n")
            log_file.write(f"Datetime: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        return log_full_name

    def append_line(self, message, log_name) -> None:
        complete_dir = os.path.join(self.log_dir,log_name)
        with open(complete_dir, "a") as log_file:
            log_file.write(f"{message}\n")

    def add_metrics(self, metric_name) -> None:
        self.metrics[metric_name] = list()

    def update_metrics(self, metric_name, metric_value) -> None:
        if metric_name not in self.metrics.keys():
            self.ERROR(f"Metric \"{metric_name}\" not found. You should use add_metrics() to add the metric then use update_metric() to record the value.")
            return
        else:
            self.metrics[metric_name].append(metric_value)













if __name__ == '__main__':
    test_logger = Logger("./logs", "test.log")
    test_logger.WARNING("TEST WARNING")
    test_logger.INFO("TEST MESSAGE")
    test_logger.ERROR("TEST ERROR")
    data = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
    test_logger.add_metrics("Accuracy")
    test_logger.add_metrics("Loss")
    test_logger.add_metrics("mIoU")
    test_logger.update_metrics("mIoU", 0.5)
    test_logger.update_metrics("Loss", 0.123)
    print(test_logger.metrics)
    print(data)