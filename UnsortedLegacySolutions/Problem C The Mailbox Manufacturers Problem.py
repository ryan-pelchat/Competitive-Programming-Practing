numberOftests = int(input())
lsTests = []
for x in range(numberOftests):
    lsTests.append(input().split())

for test in lsTests:
    ls = range(1, int(int(test[1]) / (2 ** (int(test[0]) - 1))) + 1)
    # ls = range(
    #     int(test[1]) - int(int(test[1]) / (2 ** (int(test[0]) - 1))), int(test[1]) + 1
    # )
    print(sum(ls))
