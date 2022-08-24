import sys

sys.path += ['sort_algorithms/utils']

from swap import Swap

class BubbleSort:
    """Bubble sort algorithm."""

    def setup(self):
        self.swap = Swap()

    def bubble_sort(self, data):
        self.setup()
        ordered = 0
        data_size = len(data)
        if data_size <= 1:
            return data
        while ordered < data_size:
            for i in range(data_size-ordered-1):
                if data[i] > data[i+1]:
                    self.swap.swap(data, i, i+1)
            ordered += 1
        return data
    
    def bubble_sort_optimized(self, data):
        """
        Bubble sort algorithm optimized.
        There are no swaps if the list is sorted.
        In this case, returns the list without changing it.
        """
        self.setup()
        ordered = 0
        data_size = len(data)
        if data_size <= 1:
            return data
        while ordered < data_size:
            swapped = False
            for i in range(data_size-ordered-1):
                if data[i] > data[i+1]:
                    self.swap.swap(data, i, i+1)
                    swapped = True
            ordered += 1
            if not swapped:
                return data
        return data

                

