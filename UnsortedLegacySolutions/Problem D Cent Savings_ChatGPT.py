import random

# https://chatgpt.com/share/66f88bfc-e8a8-8006-863d-998cc0fb6442

dividers = input().split()
n = int(dividers[0])
d = int(dividers[1])
cart = input().split()
prices = [int(x) for x in cart]

# n = 2000
# d = 20
# prices = [random.randint(1, 10000) for _ in range(0, n + 1)]

# n, d = input()  # Read number of items and number of dividers
# prices = [int(input()) for _ in range(n)]  # Read item prices

# Precompute prefix sums
S = [0] * (n + 1)
for i in range(1, n + 1):
    S[i] = S[i - 1] + prices[i - 1]

# Initialize DP table
INF = float("inf")
DP = [[INF] * (d + 2) for _ in range(n + 1)]
DP[0][0] = 0


# Define the rounding function
def round10(s):
    mod = s % 10
    if mod < 5:
        return s - mod
    else:
        return s + (10 - mod)


# Perform DP computation
for k in range(1, d + 2):  # for every subdivision
    for i in range(1, n + 1):  # for every prefix of list
        for j in range(i):  # for every possible division of prefix
            group_cost = round10(S[i] - S[j])
            DP[i][k] = min(DP[i][k], DP[j][k - 1] + group_cost)

# Output the minimal total cost
print(min(DP[n]))
