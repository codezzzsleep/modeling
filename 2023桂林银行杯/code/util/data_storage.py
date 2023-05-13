import os


def train_make_dir():
    tmp = os.listdir("../run/train")
    return int(tmp[len(tmp)-1])+1
def detect_make_dir():
    tmp = os.listdir("../run/detect")
    return int(tmp[len(tmp) - 1]) + 1