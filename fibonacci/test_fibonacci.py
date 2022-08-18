from fibonacci import Fibonacci
import pytest

class TestFibonacci:
    
    def test_fib_recursive(self):
        """
        Test to the Fibonacci method that calculates the Fibonacci
        number recursively as given in the mathematical definition.
        """
        fibonacci = Fibonacci()
        n = 9
        result = 34
        assert fibonacci.fib_recursive(n) == result
    
    def test_fib_dynamic_programming(self):
        """
        Test to the Fibonacci method that calculates the Fibonacci
        number using dynamic programming.
        """
        fibonacci = Fibonacci()
        n = 30
        result = 832040
        assert fibonacci.fib_dynamic_programming(n) == result
    
    def test_fib_space_optimized(self):
        """
        Test to the Fibonacci method that calculates the Fibonacci
        number storing only the two previous numbers.
        """
        fibonacci = Fibonacci()
        n = 30
        result = 832040
        assert fibonacci.fib_space_optimized(n) == result