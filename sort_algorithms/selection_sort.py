from utils.swap import swap

class SelectionSort:

    def selection_sort(self, data):
        for i in range(len(data)):
            atual = i
            for j in range(i+1, len(data)):
                if data[atual] > data[j]:
                    atual = j
            if i != atual:
                swap(data, i, atual)
        return data

if __name__ == '__main__':
    sel_sort = SelectionSort()
    data = [4,3,2,1,0,-1]
    sel_sort.selection_sort(data)
    print(data)