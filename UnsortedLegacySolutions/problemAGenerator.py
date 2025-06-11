import re
import time

sample = input()

import json
import zlib


ROOTS = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 5,
    "7": 7,
    "8": 6,
    "9": 6,
    "10": 7,
}

# Strategies:
# add 1 from previous
# concat all numbers
# multiply using factors of number
# add 1 up to number
# add up using smaller numbers (up to 2 numbers)


def strat_add1FromPrevious(number: int):
    tot = 0
    tot += ROOTS[str(number - 1)] + 1
    return tot


def strat_concatAllNumbers(number: int):
    ls = re.split("([1-9][0]+)", str(number))
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
    return ROOTS
    tot = 0
    for chr in string:
        tot += ROOTS[chr]
    return tot


def findFactors(number: int):
    factors = set()
    for i in range(2, (number // 2)):
        if number % i == 0:
            factors.add((i, number // i))
    return factors


def strat_multiplyUsingFactors(number: int):
    factors = findFactors(number)
    minimum = 9999999
    for factor in factors:
        tot = ROOTS[str(factor[0])] + ROOTS[str(factor[1])]
        if tot < minimum:
            minimum = tot
    return minimum


def strat_add1UpToNumber(number: int):
    return number


def strat_addUpUsingSmallerNumbers(number: int):
    min = 99999999
    for i in range(1, (number) // 2):
        tot = ROOTS[str(i)] + ROOTS[str(number - i)]
        if tot < min:
            min = tot
            print(
                f"for: {number}: trying factors {str(i)} and {str(number - i)} which are {ROOTS[str(i)]} and {ROOTS[str(number - i)]}"
            )
    return min


# for i in range(90000, int(sample) + 1):
for i in range(10, 1000):
    if i % 1000 == 0:
        print(f"doing {i}")
    tempValues = []

    tempValues.append(strat_add1FromPrevious(i))

    # print(f"Time taken for add1FromPrevious: {end - start}")

    tempValues.append(strat_concatAllNumbers(i))

    # print(f"Time taken for concatAllNumbers: {end - start}")

    tempValues.append(strat_multiplyUsingFactors(i))

    # print(f"Time taken for multiplyUsingFactors: {end - start}")

    tempValues.append(strat_add1UpToNumber(i))

    # print(f"Time taken for add1UpToNumber: {end - start}")
    tempValues.append(strat_addUpUsingSmallerNumbers(i))

    ROOTS[str(i)] = min(tempValues)

print(ROOTS[sample])

# print(f"Time taken for min: {end - start}")
# print("\n\n\n\n\n")

print("DONE SAVING NOWWWWW")
with open("data3.json", "w") as fl:
    json.dump(ROOTS, fl, indent=4)
print(ROOTS[sample])
