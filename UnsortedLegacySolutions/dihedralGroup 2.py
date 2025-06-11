n, m = map(int, input().split())
initialLabeling = input().split()
targetLabeling = input().split()

sequenceToCheck1 = initialLabeling + initialLabeling
sequenceToCheck2 = initialLabeling[::-1] + initialLabeling[::-1]

if targetLabeling in sequenceToCheck1:
    print("1")
    exit(0)

for i, node in enumerate(sequenceToCheck1):
    if node == targetLabeling[0]:
        if sequenceToCheck1[i : i + m] == targetLabeling:
            print("1")
            exit(0)

for i, node in enumerate(sequenceToCheck2):
    if node == targetLabeling[0]:
        if sequenceToCheck2[i : i + m] == targetLabeling:
            print("1")
            exit(0)
print("0")

# n,m=map(int,input().split());a=input().split()*2;b=a[::-1];t=input().split();print(1 if t in (a,b) else 0)
