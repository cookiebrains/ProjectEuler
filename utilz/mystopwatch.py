from stopwatch import Stopwatch
import math


class MyStopwatch:
    stopwatches = {}

    def start(self, id):
        if id in self.stopwatches:
            self.stopwatches[id].start()
        else:
            self.stopwatches[id] = Stopwatch()

    def stop(self, id):
        if id in self.stopwatches:
            self.stopwatches[id].stop()

    @staticmethod
    def get_elapsed_formatted(elapsed):
        if elapsed < 1:
            return f'{math.ceil(elapsed * 1000)} milliseconds'
        elif elapsed > 60:
            return f'{round(elapsed / 60, 2)} minutes'
        return f'{round(elapsed, 2)} seconds'

    def print_all(self):
        stopwatches_sorted = dict(sorted(self.stopwatches.items(), key=lambda item: item[1].duration))
        for id, sw in stopwatches_sorted.items():
            print(f'{id}: {MyStopwatch.get_elapsed_formatted(sw.duration)}')
