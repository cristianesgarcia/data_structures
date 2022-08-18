# Fibonacci sequence

The Fibonacci numbers, F(n), form the Fibonacci sequence, where each number is the sum of the two preceding ones.

The Fibonacci numbers may be defined as:

`F(n) = F(n-1) + F(n-2) for n > 1, with F(0) = 0 and F(1) = 1`.

The first 10 Fibonacci numbers are:

| F(0) | F(1) | F(2) | F(3) | F(4) | F(5) | F(6) | F(7) | F(8) | F(9) |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|   0  |   1  |   1  |   2  |   3  |   5  |   8  |   13 |   21 |   34 |

## Algorithms

### Recursive

This method is very simple but also very slow.
The number of operations to compute F(n) is proportional to the final numerical answer, which grows exponentially.
The Fibonacci number is calculated implementing the following formula:

`F(n) = F(n-1) + F(n-2) for n > 1, with F(0) = 0 and F(1) = 1`.

*Complexity:* exponential.

### Dynamic programming

This method stores the numbers calculated so far, this way, it avoids recalculating the same numbers.

*Complexity:* O(n)

### Space optimized

Only the previous two numbers are stored.
Those are the numbers necessary to calculate the next Fibonacci number in the series.

*Complexity:* O(n)

## Implementation

Those methods were implemented in Python in the file named fibonacci.py.

Each method has a test implemented in the file named fibonacci_test.py.

## Other algorithms/methods

### Power of the matrix

Matrix representation:

([1 1; 1 0])^n = [F(n+1) F(n); F(n) F(n-1)]


