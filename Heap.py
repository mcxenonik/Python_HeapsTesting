class Heap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)


    def _parent(self, index):
        return (index - 1) / 2


    def _left(self, index):
        return 2 * index + 1


    def _right(self, index):
        return 2 * index + 2


    def _up_heap(self, index):
        while (index != 0 and self.heap[self._parent(index)] > self.heap[index]):
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            index = self._parent(index)


    def _down_heap(self, index):
        while (self._left(index) < len(self.heap)):
            j = self._left(index)

            if (j + 1 < len(self.heap) and self.heap[j + 1] < self.heap[j]):
                j += 1

            if (self.heap[index] < self.heap[j]):
                break

            self.heap[index], self.heap[j] = self.heap[j],  self.heap[index]
            index = j


    def get_top_element(self):
        return self.heap[0]


    def delete_element(self):
        pass


    def add_element(self, value):
        self.heap.append(value)
        # print("PUSH:", value)
        self._up_heap(len(self.heap) - 1)