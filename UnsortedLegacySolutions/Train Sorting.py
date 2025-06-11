def putIn(ls, x):
    if len(ls) == 0:
        ls.append(x)
    elif ls[0] < x:
        ls.insert(0, x)
    elif ls[-1] > x:
        ls.append(x)


quantity = int(input())
ls = []
for x in range(quantity):
    ls.append(int(input()))

# outLs = [[]]
# for x in ls:
#     for y in outLs:
#         putIn(y, x)
#     outLs.append([])

# print(max([len(x) for x in outLs]))


def longest_train(weights):
    from functools import lru_cache

    n = len(weights)

    @lru_cache(maxsize=None)
    def dp(i, j, prev_weight):
        if i > j:
            return 0
        res = 0
        # Pick from left
        if weights[i] <= prev_weight:
            res = max(res, 1 + dp(i + 1, j, weights[i]))
        # Pick from right
        if weights[j] <= prev_weight:
            res = max(res, 1 + dp(i, j - 1, weights[j]))
        # Skip left
        res = max(res, dp(i + 1, j, prev_weight))
        # Skip right
        res = max(res, dp(i, j - 1, prev_weight))
        return res

    return dp(0, n - 1, float("inf"))


# Example usage:
weights = [5, 3, 4, 2, 1]
print(longest_train(ls))
