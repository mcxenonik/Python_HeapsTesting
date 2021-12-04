from random import sample
import sys

from Heap import Heap
from Heap1 import Heap1
from Heap2 import Heap2
from Heap3 import Heap3

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
 
    print("TEST ARR:")
    arr = sample(range(1, 99), 31)
    print(arr)

    print("TEST HEAP:")
    test_heap = Heap()
    test_heap.createHeap(arr)
    test_heap.printHeap()

    print("TEST HEAP2:")
    test_heap2 = Heap()
    test_heap2.betterCreateHeap(arr)
    test_heap2.printHeap()

    print("================================")
    test_heap2.printHeap3()
