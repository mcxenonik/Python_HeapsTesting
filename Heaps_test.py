from random import sample
import sys
from math import floor
from Heap1 import Heap1
from Heap2 import Heap2
from Heap3 import Heap3

from numpy import random


if __name__ == "__main__":
    sys.setrecursionlimit(100000)

    arr = sample(range(1, 10000), 500)
    # arr = random.randint(low = 1, high = 10000, size = 500)
    # print(arr)

    test_heap1 = Heap1()
    # test_heap2 = Heap2()
    # test_heap3 = Heap3()
    
    for i in arr:
        print("BEF ADD:", test_heap1.heap)
        test_heap1.push(i)
        #test_heap2.push(i)
        #test_heap3.push(i)



    print("XXX2")
    test_heap1.display()
    # print()
    # test_heap2.display()
    # print()
    # test_heap3.display()
