"""
Problem Title: 70. Climbing Stairs
Platform: Leetcode
Problem URL: https://leetcode.com/problems/climbing-stairs?envType=problem-list-v2&envId=dynamic-programming
Difficulty: Easy
Category: Math, Dynamic Programming, Memoization

Driver: Ryan
Navigator: Ben
Date Solved: 2025-08-20
Language: Python3

Problem Summary:
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Example 1:

    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

    Example 2:

    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

    Constraints:

        1 <= n <= 45

Approach:
    - strategy
        - Create a 1D array to memoize previous results to calculate future results
            - For any given stair n, you can reach it from n-1 stair ways and n-2 stair ways
            - Add all the ways from the 2 previous stairs to get how many ways for the current stair
    - technique (two pointers, recursion, BFS, etc...)
        - 1D Memoization array
    - why did you choose it?
        - Needed to build upon previous results efficiently
    - edge cases considered?
        - 0th, 1st, 2nd stairs in calculations when n is smaller than 2

Time Complexity: 0(N)
Space Complexity: 0(N)

Notes:
"""

from typing import *


class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0 for i in range(n + 1)]  # initialize 1D array for DP
        arr[0] = 1  # initialize first value
        arr[1] = 1  # init second value

        for i in range(2, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2]

        return arr[-1]
