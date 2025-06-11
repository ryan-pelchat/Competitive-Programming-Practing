"""
https://open.kattis.com/problems/addemup

Strategy:
This is a variation on the 2 pointer problem.



"""


def main(cardNum, target, cards):
    conversion = {"1": "1", "2": "2", "5": "5", "6": "9", "8": "8", "9": "6", "0": "0"}

    IDCOUNT = 0
    # 3, 4, 7
    ls = []
    for card in cards:
        ls.append((int(card), IDCOUNT))
        tempNum = ""
        if "3" not in card and "4" not in card and "7" not in card:
            for charac in card:
                tempNum += conversion[charac]
            tempNum = int(tempNum[::-1])
            ls.append((tempNum, IDCOUNT))
        IDCOUNT += 1
    ls.sort(key=lambda x: x[0])
    p1 = 0
    p2 = len(ls) - 1

    while p1 != p2:
        if ls[p1][0] + ls[p2][0] == target:
            if ls[p1][1] != ls[p2][1]:
                # print(f"{ls[p1]} \t {ls[p2]}")
                return True
            else:
                p1 += 1
        elif ls[p1][0] + ls[p2][0] < target:
            p1 += 1
        elif ls[p1][0] + ls[p2][0] > target:
            p2 -= 1
    # print(f"{ls[p1]} \t {ls[p2]}")
    return False


if __name__ == "__main__":
    cardNum, target = map(int, input().split())
    cards = input().split()
    result = main(cardNum, target, cards)
    if result:
        print("YES")
    else:
        print("NO")
