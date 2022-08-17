from fibonacci import Fibonacci
from timeit import default_timer as timer

class FibonacciTest:
    
    def __init__(self):
        self.fibonacci = Fibonacci()
        self.n = 30
        self.result = 832040

    def fib_recursive_test(self):
        """
        Test to the Fibonacci method that calculates the Fibonacci
        number recursively as given in the mathematical definition.
        """
        start = timer()
        fib_number = self.fibonacci.fib_recursive(self.n)
        print('Fibonacci number calculated recursively.')
        print(f'Elapsed time: {timer()- start} s.')
        self._test_success(fib_number)
    
    def fib_dynamic_programming_test(self):
        """
        Test to the Fibonacci method that calculates the Fibonacci
        number using dynamic programming.
        """
        start = timer()
        fib_number = self.fibonacci.fib_dynamic_programming(self.n)
        print('Fibonacci number calculated using dynamic programming.')
        print(f'Elapsed time: {timer()- start} s.')
        self._test_success(fib_number)
    
    def fib_space_optimized(self):
        """
        Test to the Fibonacci method that calculates the Fibonacci
        number storing only the two previous numbers.
        """
        start = timer()
        fib_number = self.fibonacci.fib_space_optimized(self.n)
        print('Fibonacci number calculated with space optimization.')
        print(f'Elapsed time: {timer()- start} s.')
        self._test_success(fib_number)

    def _test_success(self, fib_number):
        if fib_number == self.result:
            print('SUCCESS!')
            print(f'F({self.n}) = {fib_number}')
            return True
        else:
            print('ERROR!')
            return False

if __name__ == '__main__':
    # Make an instance of the class and run the tests
    fib_test = FibonacciTest()
    fib_test.fib_recursive_test()
    fib_test.fib_dynamic_programming_test()
    fib_test.fib_space_optimized()