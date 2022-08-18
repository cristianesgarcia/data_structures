class Fibonacci:

    def __init__(self):
        self.counter = 0
    
    def fib_recursive(self, n):
        """
        Calculates the Fibonacci number recursively as given in the 
        mathematical definition.
        F(n) = F(n-1) + F(n-2) for n > 1, where F(0) = 0 and F(1) = 1
        """
        self.counter += 1
        if n < 0:
            return None
        elif n == 0:
            return 0
        elif n < 3:
            return 1
        else:
            return self.fib_recursive(n-1) + self.fib_recursive(n-2)
    
    def fib_dynamic_programming(self, n):
        """
        Stores the numbers calculated, so there is no need to calculate
        the same number twice.
        """
        if n < 0:
            return None
        
        # stores the two first numbers in a list
        fib_sequence = [0, 1]

        for i in range(2, n+1):
            fib_sequence.append(fib_sequence[i-1]+fib_sequence[i-2])
        
        return fib_sequence[n]
    
    def fib_space_optimized(self, n):
        """
        Stores only the two previous numbers calculated.
        Those two numbers are the only ones necessary to calculate the
        next Fibonacci number.
        """
        if n < 0:
            return None
        
        j = 1
        i = 0
        for k in range(1, n+1):
            t = i + j
            i = j
            j = t
        
        return i

    
    
