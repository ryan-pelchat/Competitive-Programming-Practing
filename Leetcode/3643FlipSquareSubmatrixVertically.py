"""
Problem Title: 3643. Flip Square Submatrix Vertically
Platform: Leetcode
Problem URL: https://leetcode.com/problems/flip-square-submatrix-vertically
Difficulty: Easy
Category: Contest 462

Driver: Ryan
Navigator: Ben
Date Solved: 2025-08-13
Language: Python3

Problem Summary:
    You are given an m x n integer matrix grid, and three integers x, y, and k.

    The integers x and y represent the row and column indices of the top-left corner of a square submatrix and the integer k represents the size (side length) of the square submatrix.

    Your task is to flip the submatrix by reversing the order of its rows vertically.

    Return the updated matrix.

Approach:
    - Indexed through the submatrix
        - used a temporary list to reverse the column
        - modified original grid with reversed colum
    - returned new grid

Time Complexity: 0(k^2)
Space Complexity: 0(k^2)

Notes:
    -
"""

from typing import *


class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        for col in range(k):
            # get all the values in the column
            tempCol = []
            for row in range(k):
                tempCol.append(grid[row + x][col + y])
            tempCol.reverse()
            # modify the old values into the reversed ones
            for row in range(k):
                grid[row + x][col + y] = tempCol[row]
        return grid
