"""
Problem Title:
Platform:
Problem URL:
Difficulty:
Category:

Driver:
Navigator:
Date Solved:
Language: Python3

Problem Summary:
    ...

Approach:
    - strategy
    - technique (two pointers, recursion, BFS, etc...)
    - why did you choose it?
    - edge cases considered?

Time Complexity: 0(...)
Space Complexity: 0(...)

Notes:
    -
"""

import itertools

x = int(input())
hand = list(map(int, input().split()))
deck = []

for i in range(1, 10):
    deck.extend([i for _ in range(4)])

print(deck)


def handEvaluator(x: int, hand: list[int]) -> tuple[int, list]:
    """
    evaluates the hand and returns the value and the hand in a tuple
    """
    iterations = list(itertools.combinations(hand))
    highestHand = []
    highestValue = -1
