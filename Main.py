import matplotlib.pyplot as plt

from Heap import Heap
from Utils import Utils



def run(list_of_lists):
    Utils.start_measurements(Heap, Heap.createHeap, list_of_lists)

    # Utils.start_measurements(Heap2, Heap2.createHeap, list_of_lists)

    plt.close()

    Utils.start_measurements(Heap, Heap.betterCreateHeap, list_of_lists)

    # Utils.start_measurements(Heap2, Heap2.betterCreateHeap, list_of_lists)

    plt.close()

    Utils.start_measurements(Heap, Heap.deleteTopElement, list_of_lists)

    # Utils.start_measurements(Heap2, Heap2.deleteTopElement, list_of_lists)

    
if __name__ == "__main__":
    # list_of_lists = Utils.generate_list_of_lists(1000, 200000, 5000)
    list_of_lists = Utils.generate_list_of_lists(1000, 200000, 5000)

    run(list_of_lists)
