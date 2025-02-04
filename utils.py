import time

import torch
import random
import numpy as np
import matplotlib.pyplot as plt


def get_device():
    """
    Automatically return the device for training
    (Use GPU when cuda is available else CPU)
    :return Training device
    """
    if torch.cuda.is_available():
        return torch.device('cuda')
    else:
        return torch.device('cpu')


def print_current_torch_version():
    """
    Query the current PyTorch version
    :return:
    """
    print("The current torch version is", torch.__version__)


def set_training_seed(random_seed: int):
    """
    Set the random seed for reproducible results.
    :param random_seed:
    :return:
    """
    print(f"Setting Random Seed as {random_seed}")
    random.seed(random_seed)
    np.random.seed(random_seed)
    torch.manual_seed(random_seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(random_seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    print(f"Successfully Set Random Seed!")


def plot_initializer():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False


class Chart:
    def __init__(self, x_label: str, y_label: str, title: str, figure_size: tuple):
        plt.ion()
        self.fig, self.ax = plt.subplots(figsize=figure_size)
        self.ax.set_title(title)
        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)
        self.ax.grid(True)
        self.line = None

    def draw_line_chart(self, x_data: list, y_data: list):
        if self.line is None:
            self.line, = self.ax.plot(x_data, y_data, '-')
        else:
            self.line.set_data(x_data, y_data)

        self.ax.relim()
        self.ax.autoscale_view()
        plt.draw()
        plt.pause(0.1)


