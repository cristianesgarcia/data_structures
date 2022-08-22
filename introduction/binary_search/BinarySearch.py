class BinarySearch:

    def binary_search(self, data, target, low, high):
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
                return self.binary_search(data, target, low, mid-1)
            else:
                return self.binary_search(data, target, mid+1, high)
