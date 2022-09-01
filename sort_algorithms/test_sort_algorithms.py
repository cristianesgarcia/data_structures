from sort_algorithms import SortAlgorithms
import pytest

class TestSortAlgorithms:

    def setup(self):
        self.algorithms = SortAlgorithms()

    ####################################################################
    #### Tests for selection sort
    ####################################################################
    def test_selection_sort_unsorted(self):
        data = [3,5,0,1,2,-3,-7]
        result = data.copy()
        result.sort()
        assert self.algorithms.selection_sort(data) == result

    def test_selection_sort_sorted(self):
        data = list(range(11))
        result = data.copy()
        assert self.algorithms.selection_sort(data) == result

    def test_selection_sort_empty(self):
        data = []
        result = []
        assert self.algorithms.selection_sort(data) == result

    def test_selection_sort_single_element(self):
        data = [10]
        result = [10]
        assert self.algorithms.selection_sort(data) == result

    ####################################################################
    #### Tests for bubble sort
    ####################################################################
    def test_bubble_sort_unsorted(self):
        data = [123,87,-12,-9,4,23,56,15]
        result = data.copy()
        result.sort()
        assert self.algorithms.bubble_sort(data) == result
    
    def test_bubble_sort_sorted(self):
        data = list(range(101))
        result = data.copy()
        assert self.algorithms.bubble_sort(data) == result
    
    def test_bubble_sort_empty_list(self):
        data = []
        result = []
        assert self.algorithms.bubble_sort(data) == result
    
    def test_bubble_sort_single_element(self):
        data = [12]
        result = [12]
        assert self.algorithms.bubble_sort(data) == result
    
    ####################################################################
    #### Tests for optimized bubble sort
    ####################################################################
    def test_bubble_sort_optimized_unsorted(self):
        data = [123,87,-12,-9,4,23,56,15]
        result = data.copy()
        result.sort()
        assert self.algorithms.bubble_sort_optimized(data) == result
    
    def test_bubble_sort_optimized_sorted(self):
        data = list(range(101))
        result = data.copy()
        assert self.algorithms.bubble_sort_optimized(data) == result
    
    def test_bubble_sort_optimized_empty_list(self):
        data = []
        result = []
        assert self.algorithms.bubble_sort_optimized(data) == result
    
    def test_bubble_sort_optimized_single_element(self):
        data = [12]
        result = [12]
        assert self.algorithms.bubble_sort_optimized(data) == result


    ####################################################################
    #### Tests for insertion sort
    ####################################################################
    def test_insertion_sort_unsorted(self):
        data = [5,20,4,3,18]
        result = data.copy()
        result.sort()
        assert self.algorithms.insertion_sort(data) == result
    
    def test_insertion_sort_sorted(self):
        data = list(range(21))
        result = data.copy()
        assert self.algorithms.insertion_sort(data) == result
    
    def test_insertion_sort_empty(self):
        data = []
        result = []
        assert self.algorithms.insertion_sort(data) == result
    
    def test_insertion_sort_single_element(self):
        data = [5]
        result = [5]
        assert self.algorithms.insertion_sort(data) == result
    
    def test_insertion_sort_repeated_elements(self):
        data = [5,20,4,4,0,3,18,18]
        result = data.copy()
        result.sort()
        assert self.algorithms.insertion_sort(data) == result

    ####################################################################
    #### Tests for quick sort
    ####################################################################    
    def test_quick_sort_unsorted(self):
        data = [12,19,17,18,0,-12,13,16]
        result = data.copy()
        result.sort()
        start = 0
        end = len(data) - 1
        assert self.algorithms.quick_sort(data, start, end) == result
    
    def test_quick_sort_sorted(self):
        data = list(range(20))
        result = data.copy()
        start = 0
        end = len(data) - 1
        assert self.algorithms.quick_sort(data, start, end) == result

    def test_quick_sort_empty_list(self):
        data = []
        result = []
        start = 0
        end = 0
        assert self.algorithms.quick_sort(data, start, end) == result

    def test_quick_sort_single_element(self):
        data = [1]
        result = [1]
        start = 0
        end = len(data) - 1
        assert self.algorithms.quick_sort(data, start, end) == result

    def test_quick_sort_repeated_elements(self):
        data = [5,20,4,4,0,3,18,18,0,-12,-20,-12]
        result = data.copy()
        result.sort()
        start = 0
        end = len(data) - 1
        assert self.algorithms.quick_sort(data, start, end) == result

    ####################################################################
    #### Tests for merge sort
    ####################################################################

    def test_merge_sort_unsorted(self):
        data = [12,19,17,18,0,-12,13,16]
        result = data.copy()
        result.sort()
        assert self.algorithms.merge_sort(data) == result
    
    def test_merge_sort_sorted(self):
        data = list(range(101))
        result = data.copy()
        assert self.algorithms.merge_sort(data) == result

    def test_merge_sort_empty_list(self):
        data = []
        result = []
        assert self.algorithms.merge_sort(data) == result

    def test_merge_sort_single_element(self):
        data = [12]
        result = [12]
        assert self.algorithms.merge_sort(data) == result
    
    def test_merge_sort_repeated_elements(self):
        data = [12,19,17,18,0,-12,13,16,-12,0,0,17]
        result = data.copy()
        result.sort()
        assert self.algorithms.merge_sort(data) == result

    def test_merge_sort_index_unsorted(self):
        data = [12,19,17,18,0,-12,13,16]
        result = data.copy()
        result.sort()
        assert self.algorithms.merge_sort_index(data) == result
    
    def test_merge_sort_index_sorted(self):
        data = list(range(101))
        result = data.copy()
        assert self.algorithms.merge_sort_index(data) == result

    def test_merge_sort_index_empty_list(self):
        data = []
        result = []
        assert self.algorithms.merge_sort_index(data) == result

    def test_merge_sort_index_single_element(self):
        data = [12]
        result = [12]
        assert self.algorithms.merge_sort_index(data) == result
    
    def test_merge_sort_index_repeated_elements(self):
        data = [12,19,17,18,0,-12,13,16,-12,0,0,17]
        result = data.copy()
        result.sort()
        assert self.algorithms.merge_sort_index(data) == result




