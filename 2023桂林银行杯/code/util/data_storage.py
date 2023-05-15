import os


def train_make_dir():
    base = "../run/train/"
    tmp = os.listdir(base)
    path = base + str(len(tmp)+1)
    os.mkdir(path)
    return len(tmp)+1


def detect_make_dir():
    base = "../run/detect/"
    tmp = os.listdir(base)
    path = base + str(len(tmp)+1)
    os.mkdir(path)
    return len(tmp)+1
