from IndexMin import IndexMin
import pytest

class TestIndexMin:
    def test_my_index_of_min_empty(self):
        index_min = IndexMin()
        l = []
        result = 'The list is empty.'
        assert index_min.my_index_of_min(l) == result
    
    def test_my_index_of_min_end(self):
        index_min = IndexMin()
        l = [1, 2, 18, -1, -10, -100]
        result = 5
        assert index_min.my_index_of_min(l) == result
    
    def test_my_index_of_min_middle(self):
        index_min = IndexMin()
        l = [1, 2, 18, -1, -10, -100, 12, 56]
        result = 5
        assert index_min.my_index_of_min(l) == result
    
    def test_my_index_of_min_single(self):
        index_min = IndexMin()
        l = [1]
        result = 0
        assert index_min.my_index_of_min(l) == result