from math import floor, ceil


class Heap3:
    def __init__(self):
        self.heap = []
        self.heap.append(0)


    def push(self, value):
        self.heap.append(value)
        self._check(value)


    def _check(self, value):
        child_index = self.heap.index(value)

        if (child_index + 1) % 3 == 0:
            parent_index = ceil(child_index / 3)
        elif (child_index - 1) % 3 == 0:
            parent_index = floor(child_index / 3)
        elif child_index % 3 == 0:
            parent_index = child_index // 3

        # if (parent_index != 0 and self.heap[child_index] > self.heap[parent_index]):            # MAX HEAP
        if (parent_index != 0 and self.heap[child_index] < self.heap[parent_index]):              # MIN HEAP                                       
            self.heap[child_index], self.heap[parent_index] = self.heap[parent_index],  self.heap[child_index]
            self._check(value)


    def display(self):
        previous_pointer = 1
        line_pointer = 1
        while line_pointer <= len(self.heap):
            for element in range(previous_pointer, line_pointer):
                print(self.heap[element], end = " ")
            print()
            previous_pointer = line_pointer
            if line_pointer * 3 > len(self.heap):
                for element in range(line_pointer, len(self.heap)):
                    print(self.heap[element], end = " ")
            line_pointer = line_pointer * 3 - 1