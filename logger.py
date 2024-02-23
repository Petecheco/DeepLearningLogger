import os
import time
import datetime


date = str(datetime.date.today())
print(date)
date_time = date[2:].replace("-","_")
print(date_time)

class Logger:
    def __init__(self, experiment_name, save_dir):
        self.experiment_name = experiment_name
        self.save_dir = save_dir
        self.date = self.get_date()
        self.log_file = save_dir + "_" + self.date + "_" + experiment_name
        # Create logger folder
        self.print_message("Creating log file...")
        if not os.path.exists(self.log_file):
            os.makedirs(self.log_file)

    def get_date(self):
        raw_date = str(datetime.date.today())
        formatted_date_time = raw_date[2:].replace("-", "_")
        return formatted_date_time

    def print_message(self, message):
        print(message)


mylog = Logger("test_log", "logger")