import time

import torch
import random
import numpy as np
import matplotlib.pyplot as plt


def get_device():
    """
    自动选择使用CPU或GPU训练
    :return 返回训练时的设备
    """
    if torch.cuda.is_available():
        return torch.device('cuda')
    else:
        return torch.device('cpu')


def print_current_torch_version():
    """
    查询当前pytorch版本
    :return:
    """
    print("The current torch version is", torch.__version__)


def set_training_seed(random_seed: int):
    """
    设定训练时候的随机种子，方便重复实验
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
        # 设置标题和坐标轴标签
        self.ax.set_title(title)
        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)
        self.ax.grid(True)
        self.line = None

    def draw_line_chart(self, x_data: list, y_data: list):
        # 更新数据
        if self.line is None:
            self.line, = self.ax.plot(x_data, y_data, '-')
        else:
            # 更新数据
            self.line.set_data(x_data, y_data)

            # 重置数据范围和自动缩放
        self.ax.relim()
        self.ax.autoscale_view()
        # 重绘
        plt.draw()
        plt.pause(0.1)


if __name__ == '__main__':
    x_data = []
    y_data = []
    plot_initializer()
    new_chart = Chart("中文x", "y", "title", (10, 5))
    for i in range(100):
        x_data.append(i)
        y_data.append(i ** 2)  # 示例数据，根据实际情况修改
        new_chart.draw_line_chart(x_data, y_data)
