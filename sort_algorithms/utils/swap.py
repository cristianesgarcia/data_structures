class Swap:

    def swap(self, data, i, j):
        aux = data[i]
        data[i] = data[j]
        data[j] = aux