from insertion_sort import InsertionSort
import pytest

class TestInsertionSort:
    def setup(self):
        self.algorithm = InsertionSort()

    def test_insertion_sort_unsorted(self):
        data = [5,20,4,3,18]
        result = data.copy()
        result.sort()
        assert self.algorithm.insertion_sort(data) == result
    
    def test_insertion_sort_sorted(self):
        data = list(range(21))
        result = data.copy()
        assert self.algorithm.insertion_sort(data) == result
    
    def test_insertion_sort_empty(self):
        data = []
        result = []
        assert self.algorithm.insertion_sort(data) == result
    
    def test_insertion_sort_single_element(self):
        data = [5]
        result = [5]
        assert self.algorithm.insertion_sort(data) == result
    
    def test_insertion_sort_repeated_elements(self):
        data = [5,20,4,4,0,3,18,18]
        result = data.copy()
        result.sort()
        assert self.algorithm.insertion_sort(data) == result
    
    