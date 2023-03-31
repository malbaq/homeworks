class MaxValueReachedException(Exception):
    pass

class Counter:
    def __init__(self, start=0, stop=None) -> None:
        self.start = start
        self.stop = stop
    
    def increment(self):
        if self.stop != None:
            if self.start < self.stop:
                self.start += 1
            else:
                raise MaxValueReachedException
        else:
            self.start += 1

    def get(self):
        return self.start

try:
    counter = Counter(4, 3)
    counter.increment()
    print(counter.get())
except MaxValueReachedException:
    print('Max value reached')
