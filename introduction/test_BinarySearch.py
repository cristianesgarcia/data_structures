from BinarySearch import BinarySearch
import pytest

class TestBinarySearch:
    
    def setup(self):
        self.seq_search = BinarySearch()
        self.data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]

    def test_binary_search_end(self):
        self.setup()
        target = 37
        result = True
        assert self.seq_search.binary_search(self.data, target, 0, len(self.data)) == result
    
    def test_binary_search_empty(self):
        self.setup()
        self.data = []
        target = 65
        result = False
        assert self.seq_search.binary_search(self.data, target, 0, len(self.data)) == result
    
    def test_binary_search_ini(self):
        self.setup()
        target = 2
        result = True
        assert self.seq_search.binary_search(self.data, target, 0, len(self.data)) == result

    def test_binary_search_middle(self):
        self.setup()
        target = 22
        result = True
        assert self.seq_search.binary_search(self.data, target, 0, len(self.data)) == result

    def test_binary_search_not_exists(self):
        self.setup()
        target = 102
        result = False
        assert self.seq_search.binary_search(self.data, target, 0, len(self.data)) == result
