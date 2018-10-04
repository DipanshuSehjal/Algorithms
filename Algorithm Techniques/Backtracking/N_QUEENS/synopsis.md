# Problem Statement
A famous problem: The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.

## External References:
https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/

https://see.stanford.edu/materials/icspacs106b/H19-RecBacktrackExamples.pdf

https://www.youtube.com/watch?v=xouin83ebxE

https://en.wikipedia.org/wiki/Eight_queens_puzzle

## Backtracking Algorithm
The idea is to place queens one by one in different columns, starting from the leftmost column. When we place a queen in a column, we check for clashes with already placed queens. In the current column, if we find a row for which there is no clash, we mark this row and column as part of the solution. If we do not find such a row due to clashes then we backtrack and return false.