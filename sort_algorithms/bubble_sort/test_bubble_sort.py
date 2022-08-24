from bubble_sort import BubbleSort
import pytest

class TestBubbleSort():

    def setup(self):
        self.algorithm = BubbleSort()
    
    # Tests for the bubble sort algorithm
    def test_bubble_sort_unsorted(self):
        data = [123,87,-12,-9,4,23,56,15]
        result = data.copy()
        result.sort()
        assert self.algorithm.bubble_sort(data) == result
    
    def test_bubble_sort_sorted(self):
        data = list(range(101))
        result = data.copy()
        assert self.algorithm.bubble_sort(data) == result
    
    def test_bubble_sort_empty_list(self):
        data = []
        result = []
        assert self.algorithm.bubble_sort(data) == result
    
    def test_bubble_sort_single_element(self):
        data = [12]
        result = [12]
        assert self.algorithm.bubble_sort(data) == result
    
    # Tests for the optimized bubble sort algorithm
    def test_bubble_sort_optimized_unsorted(self):
        data = [123,87,-12,-9,4,23,56,15]
        result = data.copy()
        result.sort()
        assert self.algorithm.bubble_sort_optimized(data) == result
    
    def test_bubble_sort_optimized_sorted(self):
        data = list(range(101))
        result = data.copy()
        assert self.algorithm.bubble_sort_optimized(data) == result
    
    def test_bubble_sort_optimized_empty_list(self):
        data = []
        result = []
        assert self.algorithm.bubble_sort_optimized(data) == result
    
    def test_bubble_sort_optimized_single_element(self):
        data = [12]
        result = [12]
        assert self.algorithm.bubble_sort_optimized(data) == result
