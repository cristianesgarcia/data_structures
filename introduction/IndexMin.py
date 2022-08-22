class IndexMin:

    def index_of_min(self, l):
        """
        The book's implementation to search for the index of the minimum
        value in an unordered list.
        The first two lines are executed only once, so, they are discounted.
        Within the loop are three more instructions. Of these, the 
        comparison in the if statement and the increment of curr_index
        execute on each pass through the loop. There are no nested or
        hidden loops in these instructions. This algorithm must visit
        every item in the list to guarantee that it has located the
        position of the minimum item. This work is actually done in the
        comparison within the if statement. Thus, the algorithm must
        make n - 1 comparisons for a list of size n.
        Therefore, the algorithm's complexity is O(n).
        """
        index_min = 0
        curr_index = 1
        while curr_index < len(l):
            if l[curr_index] < l[index_min]:
                index_min = curr_index
            curr_index += 1
        return index_min

    def my_index_of_min(self, l):
        """
        Search algorithm (my implementation). This algorithm search for
        the index of the minimum value in an unordered list.
        The first six lines are executed only once. So, I am discounting
        then in the complexity count. Inside the for loop, there is an
        if statement that is executed n (size of the list) times.
        Therefore, the algorithm must take n-1 comparisons, so, the 
        algorithm's complexity is linear, that is, O(n).
        """
        list_size = len(l)
        if list_size == 0:
            return 'The list is empty.'
        elif list_size == 1:
            return 0
        i_min = 0
        for i in range(1, list_size):
            if l[i] < l[i_min]:
                i_min = i
        return i_min