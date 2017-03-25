# python3
# import argparse # remove for submission

class OneBasedIndex:
  def __init__(self, list):
    self.list = list

  def __getitem__(self, index):
    return self.list[index - 1]

  def __setitem__(self, index, value):
    self.list[index - 1] = value

  def __len__(self):
      return len(self.list)

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  # def ReadData(self):
  #   # remove before submission
  #   # parser = argparse.ArgumentParser()
  #   # parser.add_argument("filename", help="The filename to be processed")
  #   # args = parser.parse_args()
  #   # lines = list()
  #   # if args.filename:
  #   #     with open(args.filename) as f:
  #   #         for line in f:
  #   #                 lines.append(line)
  #   # end remove before submission
  #   n = int(lines[0])
  #   self._data = OneBasedIndex([int(s) for s in lines[1].split()])
  #   assert n == len(self._data)


  def ReadData(self):
    n = int(input())
    self._data = OneBasedIndex([int(s) for s in input().split()])
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])


  def swap(self, index, minIndex):
    tempVar = self._data[index]
    self._data[index] = self._data[minIndex]
    self._data[minIndex] = tempVar
    self._swaps.append((index - 1, minIndex - 1))


  def SiftDown(self, index):
    minIndex = index
    leftChildIndex = 2 * index
    if leftChildIndex <= len(self._data) and self._data[leftChildIndex] < self._data[minIndex]:
      minIndex = leftChildIndex
    rightChildIndex = (2 * index) + 1
    if rightChildIndex <= len(self._data) and self._data[(2 * index) + 1] < self._data[minIndex]:
      minIndex = rightChildIndex

    if minIndex is not index:
      self.swap(index, minIndex)
      self.SiftDown(minIndex)

  def BuildHeap(self):
      n = len(self._data)
      startingIndex = n // 2

      while startingIndex > 0:
        self.SiftDown(startingIndex)
        startingIndex -= 1


  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
