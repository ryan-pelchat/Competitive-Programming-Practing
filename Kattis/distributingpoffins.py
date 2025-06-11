"""
Problem Title: distributingpoffins
Platform: Kattis
Problem URL: https://open.kattis.com/problems/distributingpoffins?editresubmit=17545562
Difficulty: 1.9 Easy
Category: N/A

Driver: Ryan
Navigator: Ben
Date Solved: June 11 2025
Language: Python3

Problem Summary:
    There are M poffins, and N pokemon.

    Given M and N, and the following procedure:
        1. If the current Pokemon doesn’t have a poffin, skip the following steps and move on to the next Pokemon in the line.

        2. Take one poffin from the current Pokemon.

        3. Give that poffin to the Pokemon with the least number of poffins (it might be the same Pokemon you took the poffin from).
            If there are multiple Pokemon with the least number of poffins, you may pick any of them to give the poffin to.

    What is the minimum difference between the pokemon that has the most and the least amount of poffins over all possible distributions
    of poffins to pokemons?

Approach:
    - The smallest difference will result when every pokemon has equal amounts of poffins
    - Therefore:
        - if the number of poffins is divisible without a remainder by the amount of pokemons then there would be no difference (0)
        - if the number of poffins in NOT divisible without a remainder by the amount of pokemons then there would be a difference (1)

Time Complexity: 0(1)
Space Complexity: 0(1)

Notes:
    -
"""

n, m = map(int, input().split())

if m % n != 0:
    print("1")
else:
    print("0")
