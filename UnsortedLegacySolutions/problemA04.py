import re

sample = int(input())

ROOTS = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 5, 7: 6, 8: 6, 9: 6, 10: 7}
# for x in range(1, sample + 1):
#     ROOTS[x] = x


def findFactors(number: int):
    factors = set()
    for i in range(2, (int(number**0.5))):
        if number % i == 0:
            factors.add((i, number // i))
    return factors


def strat_multiplyUsingFactors(number: int):
    factors = findFactors(number)
    minimum = 9999999
    for factor in factors:
        tot = ROOTS[factor[0]] + ROOTS[factor[1]]
        if tot < minimum:
            minimum = tot
    return minimum


def strat_addUpUsingSmallerNumbers(number: int):
    min = 99999999
    for i in range(2, (number) // 2):
        tot = ROOTS[int(i)] + ROOTS[int(number - i)]
        if tot < min:
            min = tot
    return min


def strat_concatAllNumbers(number: int):
    ls = re.split("([1-9][0]+)", str(number))
    for x in range(ls.count("")):
        ls.remove("")
    tot = 0
    if len(ls) == 1 and "0" not in str(ls[0]):
        for chr in ls[0]:
            tot += ROOTS[int(chr)]
        return tot
    elif len(ls) == 1 and "0" in str(ls[0]):
        return ROOTS[int(str(number)[0])] + 7 * str(number).count("0")
    else:
        for x in ls:
            # print(x)
            # print("HERE")
            tot += ROOTS[int(str(x))]
        return tot


for x in range(1, sample + 1):
    ROOTS[x] = min(
        [
            strat_multiplyUsingFactors(x),
            strat_addUpUsingSmallerNumbers(x),
            strat_concatAllNumbers(x),
        ]
    )
print(ROOTS[sample])
