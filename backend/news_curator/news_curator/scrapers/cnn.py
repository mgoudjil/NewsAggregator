## https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time

from .helpers import files

def main():
    json = files.load_json(__file__)
    return "cnn file"


# import os

# print(os.getcwd())

