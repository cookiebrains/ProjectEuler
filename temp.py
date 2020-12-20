import progressbar
import time


def doStuff():
    print('hello world')


def fake_func(millis):
    time.sleep(millis / 1000)


for i in progressbar.progressbar(range(1, 11)):
    fake_func(100)

