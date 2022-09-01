import array

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

    def merge_sort(self, data):
        data_size = len(data)

        if data_size < 2:
            return data
        
        middle = data_size // 2
        list1 = data[0:middle]
        list2 = data[middle:data_size]
        self.merge_sort(list1)
        self.merge_sort(list2)
        self._merge(data, list1, list2)
        
        return data

    def _merge(self, data, list1, list2):
        i = 0
        j = 0
        while (i+j) < len(data):
            if (j == len(list2)) or (i < len(list1) and list1[i]<list2[j]):
                data[i+j] = list1[i]
                i += 1
            else:
                data[i+j] = list2[j]
                j += 1

    def merge_sort_index(self, data):
        # Uses a buffer to sort the elements during merge
        buffer = array.array('i', data)
        self._merge_sort_index_helper(data, buffer, 0, len(data)-1)
        return data
        
    def _merge_sort_index_helper(self, data, buffer, low, high):
        if low < high:
            middle = (low+high)//2
            self._merge_sort_index_helper(data, buffer, low, middle)
            self._merge_sort_index_helper(data, buffer, middle+1, high)
            self._merge_sort_index_merge(data, buffer, low, middle, high)
    
    def _merge_sort_index_merge(self, data, buffer, low, middle, high):
        index_1 = low
        index_2 = middle + 1

        for i in range(low, high+1):
            if index_1 > middle:
                buffer[i] = data[index_2]
                index_2 += 1
            elif index_2 > high:
                buffer[i] = data[index_1]
                index_1 += 1
            elif data[index_1] < data[index_2]:
                buffer[i] = data[index_1]
                index_1 += 1
            else:
                buffer[i] = data[index_2]
                index_2 += 1
        # Copy to the list the sorted elements
        for i in range(low, high+1):
            data[i] = buffer[i]

    def _swap(self, data, i, j):
        aux = data[i]
        data[i] = data[j]
        data[j] = aux