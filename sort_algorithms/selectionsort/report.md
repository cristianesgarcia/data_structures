# Sort algorithms

## Selection sort

The selection sort algorithm is a simple sorting algorithm.

This algorithm searches repeatedly for the smaller element in a list of numbers and put that element at de beginning of the list.
Therefore, the algorithm maintain two sublists: one list that is already sorted, and a second list that is unsorted.
In each iteration, the smaller element of the unsorted sublist is found and moved to the sorted sublist.

Example of the selection sort algorithm:

![Class diagram](images/selection_sort.svg)

### Complexity:

This algorithm has complexity *O(n^2)*.