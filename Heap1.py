from math import floor, ceil


class Heap1:
    def __init__(self):
        self.heap = []
        self.heap.append(0)


    def push(self, value):
        self.heap.append(value)
        print("PUSH:", value)
        self._check(value)

    def _check(self, value):
        child_index = self.heap.index(value)
        parent_index = floor(child_index / 2)
        # print(child_index)
        # print(parent_index)
    
        if (parent_index != 0):
            if (self.heap[child_index] > self.heap[parent_index]):
                temp = self.heap[child_index]
                self.heap[child_index] = self.heap[parent_index]
                self.heap[parent_index] = temp
            self._check(value)
        

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