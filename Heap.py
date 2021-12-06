from math import ceil, log


class Heap:
    def __init__(self, d_ary=2, values=None):
        self.heap = []
        self.d_ary = d_ary

        self.createHeap(values)


    def __str__(self):
        return str(self.d_ary) + "-Heap"


    def _parent(self, index):
        return int((index - 1) / self.d_ary)                 # ZWRÓĆ INDEKS RODZICA ELEMENTU O PODANYM INDEKSIE


    def _left(self, index):
        return int(self.d_ary * index + 1)                   # ZWRÓĆ INDEKS LEWEGO DZIECKA ELEMENTU O PODANYM INDEKSIE


    def _right(self, index):
        return int(self.d_ary * index + 2)                   # ZWRÓĆ INDEKS PRAWEGO DZIECKA ELEMENTU O PODANYM INDEKSIE

    
    def _3child(self, index):
        return int(self.d_ary * index + 3)


    def _4child(self, index):
        return int(self.d_ary * index + 4)


    def _upHeap(self, index):
        while (index != 0 and self.heap[self._parent(index)] > self.heap[index]):                                   # DOPÓKI WARTOŚĆ RODZICA JEST WIĘKSZA ZAMIENIAJ ELEMENT Z RODZICEM
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            index = self._parent(index)


    def _downHeap(self, index):             # TYLKO DLA BINARNEGO !!!!!!!!!!!
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
            self.heap = values.copy()
            for index in range(int((len(self.heap) - 2) / 2), -1, -1):          # ODTWARZAMY KOPIEC OD PRZEDOSTATNIEGO POZIOMU W GÓRĘ
                self._downHeap(index)

        return self


    def printHeap(self):
        print(self.heap)


    def printHeap2(self):
        counter = 1
        summ = 0

        while(summ <= len(self.heap)):
            if (summ >= len(self.heap)):
                break

            print(self.heap[summ : summ + counter])
            summ += counter
            counter *= self.d_ary


    def printHeap3(self, max_consol_width=128):                                                 # 128-135, 160-175, 192-207, 224-239 (16-31) | 128 (32-63)
        level = ceil(log((self.d_ary - 1) * len(self.heap) + 1, self.d_ary))
        text_heap = []
        valueLine = ""
        padLine = ""

        while(level != 0):
            sum_of_all_elements_to_level = int((self.d_ary**level - 1) / (self.d_ary - 1))
            number_of_elements_on_level = self.d_ary**(level - 1)

            right_element_index = sum_of_all_elements_to_level - 1
            left_element_index = sum_of_all_elements_to_level - number_of_elements_on_level
            
            for elementIndex in range(left_element_index, sum_of_all_elements_to_level):
                if (elementIndex >= len(self.heap)):
                    break
                else:
                    pad = ((max_consol_width / (number_of_elements_on_level)) - 4) / 2

                    if (elementIndex % self.d_ary == 0):
                        sign = "-"                       
                        sign2 = "\\"
                        sign3 = " "
                    elif (elementIndex % self.d_ary == 1):
                        sign = " "                       
                        sign2 = "/"
                        sign3 = "-"
                    elif (elementIndex % self.d_ary == 2):
                        sign = "-"                       
                        sign2 = "/"
                        sign3 = "-"
                    elif (elementIndex % self.d_ary == 3):
                        sign = "-"                       
                        sign2 = "\\"
                        sign3 = "-"

                    valueLine += (self._generateString(pad, " ") + 
                                  self._formatValue(self.heap[elementIndex]) + 
                                  self._generateString(pad, " "))
                    
                    if (elementIndex != 0):  
                        padLine += (self._generateString(pad, sign) + 
                                    " " + " " + sign2 + " " +
                                    self._generateString(pad, sign3))

            text_heap.append(valueLine)
            text_heap.append(padLine)
            valueLine = ""
            padLine = ""
            level -= 1

        text_heap.reverse()
        for line in text_heap:
            print(line)


    def _generateString(self, length, sign="="):
        string = ""

        for i in range(int(length)):
            string += sign

        return string


    def _formatValue(self, value):
        strValue = str(value)

        if (len(strValue) == 1):
            return " " + " " + strValue + " "
        elif (len(strValue) == 2):
            return " " + strValue + " "
        elif (len(strValue) == 3):
            return " " + strValue
        elif (len(strValue) == 4):
            return strValue


    def findMinChild(self, index):
        childs = []
        childs.append(self._left(index))
        childs.append(self._right(index))
        childs.append(self._3child(index))
        childs.append(self._4child(index))

        return min(childs)


class Heap3(Heap):
    def __init__(self, values=None):
        super().__init__(3, values)


class Heap4(Heap):
    def __init__(self, values=None):
        super().__init__(4, values)