#!/usr/bin/python3
"""
Returns the perimeter of the island described in grid.
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
"""


def island_perimeter(grid):
    """
    :param grid: a 2D array representing an island, where '1'
    represents land and '0' represents water (or sea).
    grid is a list of list of integers
    """
    length_row = len(grid)
    length_column = len(grid[0])

    p = 0
    connections = 0

    for x in range(length_row):
        for y in range(length_column):
            if grid[x][y] == 1:
                p += 4

                # Top elements check, we're not at row 0
                if x != 0 and grid[x - 1][y == 1]:
                    connections += 1

                if y != 0 and grid[x][y - 1] == 1:
                    connections += 1
    return p - (connections * 2)
