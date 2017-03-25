
class Reverse_Iter:
    def __init__(self, list):
        self.list = list
        self.i = len(list) - 1

    def __iter__(self):
        return self

    def next(self):
        if self.i >= 0:
            i = self.i
            self.i -= 1
            return self.list[i]
        else:
            raise StopIteration()



