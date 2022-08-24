from selection_sort import SelectionSort
import pytest

class TestSelectionSort:
    def setup(self):
        self.selection_sort = SelectionSort()

    def test_selection_sort_unsorted(self):
        self.setup()
        data = [3,5,0,1,2,-3,-7]
        result = data.copy()
        result.sort()
        assert self.selection_sort.selection_sort(data) == result

    def test_selection_sort_sorted(self):
        self.setup()
        data = list(range(11))
        result = data.copy()
        assert self.selection_sort.selection_sort(data) == result

    def test_selection_sort_empty(self):
        self.setup()
        data = []
        result = []
        assert self.selection_sort.selection_sort(data) == result

    def test_selection_sort_single_element(self):
        self.setup()
        data = [10]
        result = [10]
        assert self.selection_sort.selection_sort(data) == result