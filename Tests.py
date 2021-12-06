from random import sample
import sys

from Heap import Heap, Heap3, Heap4

if __name__ == "__main__":
    # sys.setrecursionlimit(100000)
 
    print("TEST ARR:")
    arr = sample(range(1, 99), 31)
    print(arr)

    print("================================================================================================")

    print("TEST HEAP:")
    test_heap = Heap()
    test_heap.createHeap(arr)
    test_heap.printHeap3()
    test_heap.printHeap2()

    # print("================================================================================================")

    # print("TEST HEAP(BC):")
    # test_heapBC = Heap()
    # test_heapBC.betterCreateHeap(arr)
    # test_heapBC.printHeap3()
    
    print("================================================================================================")

    print("TEST HEAP 3:")
    test_heap3 = Heap3()
    test_heap3.createHeap(arr)
    test_heap3.printHeap3()
    test_heap3.printHeap2()
    
    print("================================================================================================")

    print("TEST HEAP 4:")
    test_heap4 = Heap4()
    test_heap4.createHeap(arr)
    test_heap4.printHeap3()
    test_heap4.printHeap2()
