import itertools

dividers = int(input().split()[1])
cart = input().split()
cart = [int(x) for x in cart]

tot = 0
toadd = []
lastDivider = 0
for index, x in enumerate(cart):
    if dividers > 0 and int(str(tot + x)[-1]) == 4:
        toadd.append(round((tot + x), -1))
        dividers -= 1
        tot = 0
        if len(cart) - 1 < index:
            lastDivider = index + 1
    else:
        tot += x
if dividers > 0:
    tot = 0
    for index, x in enumerate(cart[lastDivider:]):
        if dividers > 0 and int(str(tot + x)[-1]) == 3:
            toadd.append(round((tot + x), -1))
            dividers -= 1
            tot = 0
            if len(cart) - 1 < index:
                lastDivider = index + 1
        else:
            tot += x
if dividers > 0:
    tot = 0
    for index, x in enumerate(cart[lastDivider:]):
        if dividers > 0 and int(str(tot + x)[-1]) == 2:
            toadd.append(round((tot + x), -1))
            dividers -= 1
            tot = 0
            if len(cart) - 1 < index:
                lastDivider = index + 1
        else:
            tot += x
if dividers > 0:
    tot = 0
    for index, x in enumerate(cart[lastDivider:]):
        if dividers > 0 and int(str(tot + x)[-1]) == 1:
            toadd.append(round((tot + x), -1))
            dividers -= 1
            tot = 0
            if len(cart) - 1 < index:
                lastDivider = index + 1
        else:
            tot += x
if dividers > 0:
    tot = 0
    for index, x in enumerate(cart[lastDivider:]):
        if dividers > 0 and int(str(tot + x)[-1]) == 0:
            toadd.append(round((tot + x), -1))
            dividers -= 1
            tot = 0
            if len(cart) - 1 < index:
                lastDivider = index + 1
        else:
            tot += x
toadd.append(round(tot, -1))
print(sum(toadd))


# dividers = 10
# cart = list(range(0, 2001))

# ls = list(range(0, len(cart)))
# combinations = list(itertools.combinations(ls, dividers + 1))


# tot = []
# temptot = 0
# print(combinations)
# ls2 = []
# for div in combinations:
#     for i in range(0, len(div) - 1):
#         ls2.append(
#             round(sum(cart[: div[i + 1]]), -1)
#             + round(sum(cart[div[i] : div[i + 1]]), -1)
#             + round(sum(cart[div[i + 1] :]), -1)
#         )
#         print(f"{ls2[-1]}\t{cart[div[i] : div[i + 1]]}\t|\t{cart[div[i + 1] :]}")
#     # for subdivision in ls2:
#     #     temptot += round(sum(subdivision), -1)
#     print(ls2)
#     # tot.append(temptot)
#     # temptot = 0

# print(min(ls2))


# print(combinations)

# ls = list(range(0, 2001))
# print(len(list(itertools.combinations(ls, 20))))

# dividerss = int(input().split()[1])
# cart = input().split()

# cart = [int(x) for x in cart]s


# def calcCart(ls: list[list[int]]) -> int:
#     tot = 0
#     for subdivision in ls:
#         tot += round(sum(subdivision), -1)
#     return tot


# def dividersFunc(ls: list[list[int]], dividers: int):
#     if dividers == 0:
#         return calcCart(ls)
#     else:
#         possibleCarts = []
#         possibleValues = []
#         for index, subdivision in enumerate(ls):
#             for i in range(1, len(subdivision)):
#                 tempLs = ls[::]
#                 tempLs.pop(index)
#                 tempSubdiv = [subdivision[:i], subdivision[i:]]
#                 tempLs.insert(index, tempSubdiv[1])
#                 tempLs.insert(index, tempSubdiv[0])
#                 possibleCarts.append([calcCart(tempLs), tempLs])
#             for cart in possibleCarts:
#                 possibleValues.append(dividersFunc(cart[1], dividers - 1))
#             return min(possibleValues)
#             # possibleCarts.sort()
#             # return dividersFunc(possibleCarts[-1][1], dividers - 1)


# print(dividersFunc([cart], dividerss))


# # def dividersFunc(ls: list[list[int]], dividers: int):
# #     if dividers == 0:
# #         return calcCart(ls)
# #     else:
# #         possibleCarts = []
# #         for index, subdivision in enumerate(ls):
# #             for i in range(1, len(subdivision)):
# #                 tempLs = ls[::]
# #                 tempLs.pop(index)
# #                 tempSubdiv = [subdivision[:i], subdivision[i:]]
# #                 tempLs.insert(index, tempSubdiv[1])
# #                 tempLs.insert(index, tempSubdiv[0])
# #                 possibleCarts.append([calcCart(tempLs), tempLs])
# #             possibleCarts.sort()
# #             return dividersFunc(possibleCarts[-1][1], dividers - 1)
