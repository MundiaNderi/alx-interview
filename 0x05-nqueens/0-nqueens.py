#!/usr/bin/python3
"""
N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.
"""

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)
except ValueError:
    print("N must be a number")
    exit(1)


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower left diagonal
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N-Queens problem using backtracking.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]

    def solve(row):
        if row == n:
            # All queens are placed, print the solution
            for row in board:
                print([i for i, x in enumerate(row) if x == 1])
            print()
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)


solve_nqueens(n)
