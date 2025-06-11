import itertools
import collections


def doesItFit(combo, allowed_letters) -> bool:
    setPool = set()
    for tup in combo:
        for charac in tup:
            if charac not in allowed_letters:
                return False
            if charac in setPool:
                return False
            else:
                setPool.add(charac)
    return True


p, t = map(int, input().split())

teamsAll = []
for i in range(t):
    teamsAll.append(input())

teamsAll = set(teamsAll)  # remove duplicates
letterPool = set(
    sorted([chr(x + 64) for x in list(range(1, p + 1))])
)  # create a list of ints representing the problems

combos = []
maxRet = 0
for i in range(1, len(teamsAll) + 1):
    for combo in list(itertools.combinations(teamsAll, i)):
        if doesItFit(combo, letterPool):
            maxRet = max(maxRet, len(combo))
print(maxRet)
