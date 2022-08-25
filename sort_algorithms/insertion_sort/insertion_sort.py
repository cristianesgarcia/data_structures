class InsertionSort:
    """
    Sort a list of elements in decreasing order.
    """
    def insertion_sort(self, data):
        for i in range(1, len(data)):
            item = data[i]
            j = i - 1
            while j >= 0 and item < data[j]:
                data[j+1] = data[j]
                j -= 1
            data[j+1] = item
        return data

if __name__ == '__main__':
    ins = InsertionSort()
    data = [5,20,-12,4,3,18,-12,-12,0]
    res = ins.insertion_sort(data)
    print(res)