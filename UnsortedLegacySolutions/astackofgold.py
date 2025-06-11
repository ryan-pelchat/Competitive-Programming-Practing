weight, stacks = map(int, input().split())

c = stacks * (stacks + 1) // 2
tung = 29260
gold = 29370
tOG = c * tung

for i in range(1, stacks + 1):
    if abs(weight - tOG) == abs((i * (gold - tung))):
        print(i)
