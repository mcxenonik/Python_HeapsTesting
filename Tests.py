from math import log2
from random import sample
import sys

from Heap import Heap
from Heap2 import Heap2
from Heap3 import Heap3
from Heap4 import Heap4

if __name__ == "__main__":
    # sys.setrecursionlimit(100000)
 
    print("TEST ARR:")
    arr = sample(range(1, 99), 67)
    print(arr)

    # print("TEST HEAP:")
    # test_heap = Heap()
    # test_heap.createHeap(arr)
    # test_heap.printHeap()

    # print("TEST HEAP2:")
    # test_heap2 = Heap()
    # test_heap2.betterCreateHeap(arr)
    # test_heap2.printHeap()

    # print("================================")
    # test_heap2.printHeap3()


    # test2 = Heap2()
    # test3 = Heap3()
    # test4 = Heap4()

    # for i in arr:
    #     test2.push(i)
    #     test3.push(i)
    #     test4.push(i)

    # test2.display()
    # test3.display()
    # test4.display()


    test_heap = Heap()
    test_heap.createHeap(arr)
    test_heap.printHeap()


    test_heap.printHeap3()
