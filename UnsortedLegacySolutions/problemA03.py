sample = input()
ROOTS = {}
import re

# add 1s
for x in [1, 11, 111, 1111, 11111]:
    ROOTS[str(x)] = len(str(x))


def generate_all_groupings(lst):
    if len(lst) == 1:
        return [[tuple(lst)]]

    result = [[tuple(lst)]]  # Include the full list as one group

    # Recursive part: split at each position and generate groupings
    for i in range(1, len(lst)):
        left_part = tuple(lst[:i])
        for right_grouping in generate_all_groupings(lst[i:]):
            result.append([left_part] + right_grouping)

    return result


def strat_concatAllNumbers(number: int):
    ls = re.split("([1-9][0]+)", str(number))
    ls2 = []
    for x in ls:
        if 0 not in x:
            for char in x:
                ls2.append(char)
        else:
            ls2.append(x)

    tupleList = []
    for i in range(1, len(ls2)):
        leftTuple = None
        rightTuple = None
        tupleList.append()

    total = 0
    for x in ls:
        tempstr = str(x)
        if "0" in tempstr:
            total += handleZeroes(tempstr)
        else:
            total += handleRegular(tempstr)
    return total


def handleZeroes(string: str):
    tot = ROOTS[str(string[0])] + 7 * string.count("0")
    return tot


def handleRegular(string: str):
    tot = 0
    for chr in string:
        tot += ROOTS[chr]
    return tot
