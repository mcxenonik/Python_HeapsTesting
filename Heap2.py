from math import floor
from Heap import Heap


class Heap2(Heap):
    def __init__(self):
        self.heap = []
    

    def _upHeap(self, index):
        if (index != 0 and self.heap[self._parent(index)] > self.heap[index]):                                      # MIN HEAP                                       
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            self._upHeap(self._parent(index))


    def display(self):
        previous_pointer = 1
        line_pointer = 1
        while line_pointer <= len(self.heap):
            for element in range(previous_pointer, line_pointer):
                print(self.heap[element], end = " ")
            print()
            previous_pointer = line_pointer
            if line_pointer * 2 > len(self.heap):
                for element in range(line_pointer, len(self.heap)):
                    print(self.heap[element], end = " ")
            line_pointer = line_pointer * 2