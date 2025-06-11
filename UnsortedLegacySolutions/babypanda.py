"""
Date: Feb 08, 2025
Link: https://open.kattis.com/problems/babypanda?tab=metadata
Authors: Ryan, Ben
Rationale:
    Note that whenever the number of slimes double, it will always result in an even number.
    Therefore, the though goes that if it is even, then the slimes doubled, if it is odd, then the
    panda sneezed. We can then work our way backwards where we divide by 2 when even and subtract 1 when odd
    (and adding 1 to our sneeze counter) until we reach 0.
"""

input = input().split()

days = int(input[0])
slimes = int(input[1])

sneezes = 0

while slimes > 0:
    if slimes % 2 == 0:
        slimes = slimes // 2
    else:
        slimes -= 1
        sneezes += 1

print(sneezes)
