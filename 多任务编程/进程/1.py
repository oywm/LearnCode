from multiprocessing import Process
import time


def test():
    print("----1-----")


if __name__ == '__main__':
    p = Process(target=test)
    p.start()
    print("--main----")




