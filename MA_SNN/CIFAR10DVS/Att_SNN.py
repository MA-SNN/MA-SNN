import os

import sys

sys.path.append(os.path.dirname("__file__"))

from CIFAR10DVS.CNN import Att_SNN


rootPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(rootPath)[0]
sys.path.append(rootPath)

from CIFAR10DVS.CNN import Config
import sys

os.environ["CUDA_VISIBLE_DEVICES"] = "3"


class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


logPath = Config.configs().recordPath
if not os.path.exists(logPath):
    os.makedirs(logPath)
sys.stdout = Logger(logPath + os.sep + "log_CIFAR10_DVS_SNN.txt")


def main():
    Att_SNN.main()


if __name__ == "__main__":
    main()
