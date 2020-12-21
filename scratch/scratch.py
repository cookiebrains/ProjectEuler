import time
import math
from stopwatch import Stopwatch
from utilz import MyStopwatch
import progressbar


def instance_count_test():
    list_of_lists = [[1], [2], [3], [2, 2], [5], [2, 3]]
    instance_counts = {}
    for inner_list in list_of_lists:
        inner_instance_counts = {}
        for num in inner_list:
            if num not in inner_instance_counts:
                inner_instance_counts[num] = 1
            else:
                inner_instance_counts[num] += 1
        for num, count in inner_instance_counts.items():
            if num not in instance_counts:
                instance_counts[num] = 1
            else:
                if count > instance_counts[num]:
                    instance_counts[num] = count


def print_elapsed(elapsed):
    if elapsed < 1:
        print(f'elapsed: {math.ceil(elapsed * 1000)} milliseconds')
        return
    print(f'elapsed: {round(elapsed, 2)} seconds')


def time_it(func):
    stopwatch = Stopwatch()
    func()
    stopwatch.stop()
    print_elapsed(stopwatch.duration)


def fake_long_running(millis):
    time.sleep(millis / 1000)


def stopwatch_test():
    time_it(lambda: fake_long_running(0.01))
    time_it(lambda: fake_long_running(1.5))


def my_stopwatch_test():
    sw = MyStopwatch()
    sw.start('all')
    sw.start('short')
    fake_long_running(10)
    sw.stop('short')
    sw.start('long')
    fake_long_running(500)
    sw.stop('long')
    sw.start('very_long')
    fake_long_running(62000)
    sw.stop('very_long')
    sw.stop('all')
    sw.print_all()


def progress_bar_test():
    for i in progressbar.progressbar(range(1, 10)):
        fake_long_running(250)


progress_bar_test()