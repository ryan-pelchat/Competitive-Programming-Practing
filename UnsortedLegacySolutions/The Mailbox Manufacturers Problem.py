import math


def mailbox(lss, newStart, firecrakers):

    ls = lss[newStart:]
    if len(ls) <= 3:
        return firecrakers
    ls2 = ls[::]
    for i in range(1, len(ls)):
        ls[i] = ls[i] + ls[i - 1]

    for i in range(len(ls) - 2, -1, -1):
        ls2[i] = ls2[i] + ls2[i + 1]

    ls3 = {}
    for i in range(1, len(ls) - 1):
        ls3[(abs(ls[i - 1] - ls2[i + 1]))] = i
    # print(ls3)
    minNum = min(list(ls3.keys()))
    return mailbox(lss, newStart + ls3[minNum], firecrakers + i + 1)
    return ls3[minNum] + newStart
    print(f"{ls3[minNum]}\t {newStart} \t {ls3[minNum]+newStart}")
    # #print(minNum)
    # print(ls[ls3[minNum]])
    # print(ls2[ls3[minNum]])

    # print(ls)
    # print(ls2)


ls = [1, 2, 3]
for i in range(1, len(ls) - 1):
    print(i)


print(mailbox(list(range(1, 74)), 0, 0))

# ans = ""
# while ans == "":
#     ans = mailbox(list(range(1, 74)), 0)


# mailbox(list(range(1, 74)), 0)
# mailbox(list(range(1, 74)), 51)
# mailbox(list(range(1, 74)), 62)
# mailbox(list(range(1, 74)), 67)
# mailbox(list(range(1, 74)), 70)
