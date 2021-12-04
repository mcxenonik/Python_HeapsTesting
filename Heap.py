class Heap:
    def __init__(self, values=None):
        self.heap = []

        self.createHeap(values)
        # self.betterCreateHeap(values)


    def __str__(self):
        return "BinaryHeap"


    def _parent(self, index):
        return int((index - 1) / 2)                 # ZWRÓĆ INDEKS RODZICA ELEMENTU O PODANYM INDEKSIE


    def _left(self, index):
        return int(2 * index + 1)                   # ZWRÓĆ INDEKS LEWEGO DZIECKA ELEMENTU O PODANYM INDEKSIE


    def _right(self, index):
        return int(2 * index + 2)                   # ZWRÓĆ INDEKS PRAWEGO DZIECKA ELEMENTU O PODANYM INDEKSIE


    def _upHeap(self, index):
        while (index != 0 and self.heap[self._parent(index)] > self.heap[index]):                                   # DOPÓKI WARTOŚĆ RODZICA JEST WIĘKSZA ZAMIENIAJ ELEMENT Z RODZICEM
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            index = self._parent(index)


    def _downHeap(self, index):
        while (self._left(index) < len(self.heap)):                                              # DOPÓKI WARTOŚĆ RODZICA JEST WIĘKSZA ZAMIENIAJ ELEMENT Z MNIEJSZYM DZIECKIEM
            j = self._left(index)

            if (j + 1 < len(self.heap) and self.heap[j + 1] < self.heap[j]):
                j += 1

            if (self.heap[index] < self.heap[j]):
                break

            self.heap[index], self.heap[j] = self.heap[j],  self.heap[index]
            index = j


    def getTopElement(self):
        if (self.heap):
            return self.heap[0]
        else:
            return None


    def deleteTopElement(self, arg=None):
        if (self.heap):
            root = self.heap[0]                 # ZAPISZ NAJMNIEJSZY ELEMENT
            self.heap[0] = self.heap[-1]        # WSTAW DO KORZENIA OSTATNI ELEMENT
            self.heap.pop()                     # USUŃ OSTATNI ELEMENT
            self._downHeap(0)                   # PRZENIEŚ ELEMENT Z KORZENIA NA WŁAŚCIWE MIEJSCE

            return root                         # ZWRÓĆ ZAPISANY NAJMNIEJSZY ELEMENT
        else:
            return None


    def addElement(self, value):
        if (value is not None):
            self.heap.append(value)                 # DODAJ ELEMENT NA KONIEC
            self._upHeap(len(self.heap) - 1)        # PRZENIEŚ OSTATNI ELEMENT NA WŁAŚCIWE MIEJSCE


    def createHeap(self, values):
        if (values is not None):
            for value in values:
                self.addElement(value)

        return self


    def betterCreateHeap(self, values):
        if (values is not None):
            self.heap = values
            for index in range(int((len(self.heap) - 2) / 2), -1, -1):          # ODTWARZAMY KOPIEC OD PRZEDOSTATNIEGO POZIOMU W GÓRĘ
                self._downHeap(index)

        return self


    def printHeap(self):
        print(self.heap)


    def printHeap2(self):
        counter = 1
        summ = 0

        while(summ <= len(self.heap)):
            print(self.heap[summ : summ + counter])
            summ += counter
            counter *= 2


    def printHeap3(self, max_consol_width=160):
        length = max_consol_width / 4
        counter = 1
        sum = 0
        line = ""

        while(sum <= len(self.heap)):
            for index in range(counter):
                if (sum + index >= len(self.heap)): break
                line += (self._generateString(length, " ") + "|" + self._generateString(length, "-") +
                         self._formatValue(self.heap[sum + index]) +
                         self._generateString(length, "-") + "|" + self._generateString(length, " "))
                
            print(line)

            sum += counter
            counter *= 2
            length /= 2
            line = ""


    def _generateString(self, length, sign="="):
        string = ""

        for i in range(int(length)):
            string += sign

        return string


    def _formatValue(self, value):
        strValue = str(value)

        if (len(strValue) == 1):
            return " " + strValue + " "
        elif (len(strValue) == 2):
            return strValue[0] + " " + strValue[1]
        elif (len(strValue) == 3):
            return strValue