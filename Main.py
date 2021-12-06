import matplotlib.pyplot as plt

from Heap import Heap, Heap3, Heap4

from Utils import Utils


def run(list_of_lists):
    Utils.start_measurements(Heap, Heap.createHeap, list_of_lists)

    Utils.start_measurements(Heap3, Heap3.createHeap, list_of_lists)

    Utils.start_measurements(Heap4, Heap4.createHeap, list_of_lists)

    plt.close()

    # Utils.start_measurements(Heap, Heap.betterCreateHeap, list_of_lists)

    # Utils.start_measurements(Heap3, Heap3.betterCreateHeap, list_of_lists)

    # Utils.start_measurements(Heap4, Heap4.betterCreateHeap, list_of_lists)

    # plt.close()

    Utils.start_measurements(Heap, Heap.deleteTopElement, list_of_lists)

    Utils.start_measurements(Heap3, Heap3.deleteTopElement, list_of_lists)

    Utils.start_measurements(Heap4, Heap4.deleteTopElement, list_of_lists)

    
if __name__ == "__main__":
    list_of_lists = Utils.generate_list_of_lists(1000, 100000, 5000)

    run(list_of_lists)
