class SortAlgorithms:

    def selection_sort(self, data):
        for i in range(len(data)):
            current = i
            for j in range(i+1, len(data)):
                if data[current] > data[j]:
                    current = j
            if i != current:
                self._swap(data, i, current)
        return data
    
    def bubble_sort(self, data):
        ordered = 0
        data_size = len(data)
        if data_size <= 1:
            return data
        while ordered < data_size:
            for i in range(data_size-ordered-1):
                if data[i] > data[i+1]:
                    self._swap(data, i, i+1)
            ordered += 1
        return data
    
    def bubble_sort_optimized(self, data):
        """
        Bubble sort algorithm optimized.
        There are no swaps if the list is sorted.
        In this case, returns the list without changing it.
        """
        ordered = 0
        data_size = len(data)
        if data_size <= 1:
            return data
        while ordered < data_size:
            swapped = False
            for i in range(data_size-ordered-1):
                if data[i] > data[i+1]:
                    self._swap(data, i, i+1)
                    swapped = True
            ordered += 1
            if not swapped:
                return data
        return data
    
    def insertion_sort(self, data):
        for i in range(1, len(data)):
            item = data[i]
            j = i - 1
            while j >= 0 and item < data[j]:
                data[j+1] = data[j]
                j -= 1
            data[j+1] = item
        return data
    
    def quick_sort(self, data, start, end):        
        if start >= end or start < 0:
                return data
            
        pos_pivot = self._partition(data, start, end)

        self.quick_sort(data, start, pos_pivot-1)
        self.quick_sort(data, pos_pivot+1, end)

        return data

    def _partition(self, data, start, end):
        position_pivot = (start+end)//2
        pivot = data[position_pivot]
        data[position_pivot] = data[end]
        data[end] = pivot
        boundary = start
        
        for i in range(start, end):
            if data[i] < pivot:
                self._swap(data, boundary, i)
                boundary += 1
        
        self._swap(data, end, boundary)
        return boundary
    
    def _swap(self, data, i, j):
        aux = data[i]
        data[i] = data[j]
        data[j] = aux