from dynamic_array import DynamicArray
import pytest

class TestDynamicArray:

    def setup(self):
        self.array = DynamicArray()
    
    def test_new_empty_array(self):
        result = 0
        assert len(self.array) == result
    
    def test_array_one_element(self):
        data = 10
        self.array.append(data)
        assert self.array[0] == data and len(self.array) == 1
    
    def test_array_multiple_elements(self):
        data = range(11)
        size_data = len(data)
        for i in data:
            self.array.append(data[i])
        assert len(self.array) == size_data and self.array[4] == data[4]
    
    def test_array_invalid_index(self):
        self.array.append(10)
        result = 'invalid index'
        assert self.array[2] == result
    

