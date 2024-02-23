import os
import time
import datetime

LOG_LEVEL = {
    'low': 0,
    'high': 1
}


class DLLogger:
    def __init__(self, experiment_name, save_dir, log_level='low'):
        self.experiment_name = experiment_name
        self.save_dir = save_dir
        self.date = self.get_write_date()
        self.log_file = save_dir + "_" + self.date + "_" + experiment_name
        self.set_log_level(log_level)
        self.content = []
        self.metrics = []
        self.log_level = LOG_LEVEL[log_level]
        self.start_time = None
        self.end_time = None
        self.duration_time = None

        # Create logger folder
        self.print_message("Creating log file...")
        if not os.path.exists(self.log_file):
            os.makedirs(self.log_file)

    def get_write_date(self):
        raw_date = str(datetime.date.today())
        formatted_date_time = raw_date[2:].replace("-", "_")
        return formatted_date_time

    def get_present_date(self):
        return datetime.datetime.now().strftime("%Y-%m-%d|%H:%M:%S")

    def print_message(self, message):
        print(message)

    def add_metrics(self, metrics):
        self.metrics.append(metrics)

    def set_log_level(self, log_level='low'):
        assert log_level in LOG_LEVEL.keys(), "Invalid logging level!"

    def start_timer(self):
        self.start_time = time.time()

    def end_timer(self):
        self.end_time = time.time()
        self.duration_time = (self.end_time - self.start_time)

    def print_duration(self, unit):
        assert self.duration_time is not None, "You must have a start_timer and end_timer to obtain the duration time"
        if unit == 's':
            print(f"The last timer cycle cost {self.duration_time} seconds to finish.")
        elif unit == 'ms':
            print(f"The last timer cycle cost {self.duration_time * 1e3} micro-seconds to finish.")
        elif unit == 'ns':
            print(f"The last timer cycle cost {self.duration_time * 1e9} nano-seconds to finish.")