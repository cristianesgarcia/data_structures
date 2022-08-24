import sys

sys.path += ['sort_algorithms/utils']

from swap import Swap

class SelectionSort:

    def selection_sort(self, data):
        swap = Swap()
        
        for i in range(len(data)):
            atual = i
            for j in range(i+1, len(data)):
                if data[atual] > data[j]:
                    atual = j
            if i != atual:
                swap.swap(data, i, atual)
        return data

if __name__ == '__main__':
    sel_sort = SelectionSort()
    data = [4,3,2,1,0,-1]
    sel_sort.selection_sort(data)
    print(data)