
def main(wireLen, d, n, birdPoss):
    addedBirds = 0
    if wireLen <= 12:
        return 0
    # check first pole
    if  n == 0 or birdPoss[0] - 6 >= d:
        birdPoss.insert(0, 6)
        addedBirds += 1

    # check last pole
    if wireLen - 6 - birdPoss[-1] >= d or len(birdPoss) == 0:
        birdPoss.append(wireLen-6)
        addedBirds += 1

    # do the middle stuff here!!!!
    for z in range(len(birdPoss)-1):
        addedBirds += ((birdPoss[z+1] - birdPoss[z])//d)-1

    return addedBirds

if __name__ == "__main__":
    wireLen, d, n = map(int, input().split())
    birdPoss = []

    for i in range(n):
        birdPoss.append(int(input()))

    birdPoss.sort()
    result = main(wireLen, d, n, birdPoss)
    print(result)
