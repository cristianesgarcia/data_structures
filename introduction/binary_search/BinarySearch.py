class BinarySearch:

    def binary_search_recursive(self, data, target, low, high):
        """
        Binary search implemented recursively.
        Data should be a list of ordered numbers.
        Returns True if target belongs to data, and False otherwise.
        """
        if low > high:
            return False
        else:
            mid = (low + high) // 2
            if mid >= len(data):
                return False
            if target == data[mid]:
                return True
            elif target < data[mid]:
                return self.binary_search_recursive(data, target, low, mid-1)
            else:
                return self.binary_search_recursive(data, target, mid+1, high)
    
    def binary_search(self, data, target):
        """
        Binary search.
        Data should be a list of ordered numbers.
        Returns True if target belongs to data, and False otherwise.
        """
        low = 0
        high = len(data) - 1
        
        if high == 0:       # Empty list
            return False
        
        while low <= high:
            mid = (low + high)//2
            if target == data[mid]:
                return True
            elif target < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return False

