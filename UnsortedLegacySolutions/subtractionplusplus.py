# https://open.kattis.com/problems/subtractionplusplusplus


def divSum(n: int):
    return n * (n + 1) // 2


def generatePossibleAns(level: int, initNum: int):
    return [_ for _ in range(initNum - divSum(level), (initNum - level + 1))]


def doYouWIN(level: int, cases: list[int]):
    # this is because the inflection point is at 2
    # if there are only edges, then we need to consider the edges
    print(cases)
    if len(cases) <= 2:
        for case in cases:
            if case == level + 2 or case == level + 3:
                return True
        return False

    for case in cases[1:-1]:
        if case == level + 2 or case == level + 3:
            return True
    return False


# n*(n+1)/2 = current
# current = int(input())


# for x in range(current):
#     if x % 2 == 0:
#         # B's Turn
#         if doYouWIN(x, generatePossibleAns(x, current)):
#             print("NO")
#         else:
#             print("YES")
#     else:
#         # A's Turn
#         if doYouWIN(x, generatePossibleAns(x, current)):
#             print("YES")
#         else:
#             print("NO")


def main(current: int):
    match current:
        case 1:
            print("YES")
            return
            # exit(0)
        case 2:
            print("NO")
            return
            # exit(0)
        case 3:
            print("NO")
            return
            # exit(0)

    temp = current
    count = 1
    while temp > count + 2:
        temp -= count
        count += 1
        print(f"temp: {temp}  \t count: {count}")

    count -= 1
    print("----------------")
    print(count)

    if count % 2 == 0:
        # B's Turn
        if doYouWIN(count, generatePossibleAns(count, current)):
            print("NO")
        else:
            print("YES")
    else:
        # A's Turn
        if doYouWIN(count, generatePossibleAns(count, current)):
            print("YES")
        else:
            print("NO")


# print(generatePossibleAns(7, 15))
# main(16)


def main2(current):
    # current = int(input())
    if current == 1:
        return "YES"
    level = 1
    count = 2
    aWin = False
    while level < current:
        level += count
        if aWin:
            count += 1
        if level < current:
            aWin = not aWin
    if aWin:
        return "YES"
    else:
        return "NO"


# for x in range(1, 21):
#     print(f"level: {x}   \t{main2(x)}")

print(main2(int(input())))


# for x in range(100):
#     print(x, end=" \t|")
#     main(x)


# arr = []
# for i in range(current):
#     # calculate and append ans to arr
#     pass
# print(count)
# print(divSum(count))
# print(generatePossibleAns(count, current))

# access -1 and determine if Alex wins

# print ans =
