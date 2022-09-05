import ctypes

class DynamicArray:
    """
    Dynamic array class: similar to a simplified Python list
    """

    def __init__(self):
        """Create an empty array"""
        self._n = 0
        self._capacity = 1
        self._array = self._make_array(self._capacity)

    def __len__(self):
        """Return the number of elements stored in the array"""
        return self._n
    
    def __getitem__(self, position):
        """Return the array's element at index position"""
        if not 0 <= position < self._n:
            return 'invalid index'
        return self._array[position]
    
    def append(self, element):
        """Append an element to the end of the array"""
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._array[self._n] = element
        self._n += 1
    
    def _resize(self, size):
        """Resize array's internal capacity"""
        array_temp = self._make_array(size)
        for i in range(self._n):
            array_temp[i] = self._array[i]
        self._array = array_temp
        self._capacity = size

    def _make_array(self, capacity):
        """Return new array with capacity 'capacity'"""
        return (capacity*ctypes.py_object)()
    

