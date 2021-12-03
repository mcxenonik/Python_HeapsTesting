class Heap:
    def __init__(self, values=None):
        self.heap = []

        if (values is not None):
            self.naive_create_heap(values)

    def _parent(self, index):
        return int((index - 1) / 2)


    def _left(self, index):
        return int(2 * index + 1)


    def _right(self, index):
        return int(2 * index + 2)


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
        root = self.heap[0]                 # ZAPISZ NAJMNIEJSZY ELEMENT
        self.heap[0] = self.heap[-1]        # WSTAW DO KORZENIA OSTATNI ELEMENT
        self.heap.pop()                     # USUŃ OSTATNI ELEMENT
        self._down_heap(0)                  # PRZENIEŚ ELEMENT Z KORZENIA NA WŁAŚCIWE MIEJSCE

        return root                         # ZWRÓĆ NAJMNIEJSZY ELEMENT


    def add_element(self, value):
        self.heap.append(value)
        self._up_heap(len(self.heap) - 1)


    def naive_create_heap(self, values):
        for value in values:
            self.add_element(value)


    def create_heap(self, values):
        self.heap = values
        for index in range(int((len(self.heap) - 2) / 2), -1, -1):
            self._down_heap(index)


    def print_heap(self):
        print(self.heap)

    def print_heap2(self):
        pass