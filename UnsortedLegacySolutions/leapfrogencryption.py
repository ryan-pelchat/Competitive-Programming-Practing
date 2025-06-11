# def oneE(plaintext):
#     ans = ""
#     for charac in plaintext:
#         if charac in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
#             ans += charac
#     ans.lower()
#     return ans


def oneD(ciphertext: str):
    return ciphertext.upper()


# def twoE(key):
#     # this is for the letters of the key
#     ans = ""
#     for charac in key:
#         ans += ord(charac)-96
#     return ans


def getIndexesRight(arr, leap):
    if len(arr) < int(leap):
        return []
    ls = []  # list of indexes that are empty
    for i, spot in enumerate(arr):
        if spot == "":
            ls.append(i)
    ls2 = list(range(int(leap) - 1, len(ls), int(leap)))  # list of indexes for leap
    return [ls[x] for x in ls2]  # returns list of indexes


def getIndexesLeft(arr, leap):
    if len(arr) < int(leap):
        return []
    ls = []  # list of indexes that are empty
    for i, spot in enumerate(arr):
        if spot == "":
            ls.append(i)
    ls2 = list(
        range(len(ls) - 1 - int(leap) + 1, -1, -int(leap))
    )  # list of indexes for leap
    return [ls[x] for x in ls2]  # returns list of indexes


def getIndexesRightDecrypt(arr, leap):
    if len(arr) < int(leap):
        return []
    ls = []  # list of indexes that are empty
    for i, spot in enumerate(arr):
        if spot != "":
            ls.append(i)
    ls2 = list(range(int(leap) - 1, len(ls), int(leap)))  # list of indexes for leap
    return [ls[x] for x in ls2]  # returns list of indexes


def getIndexesLeftDecrypt(arr, leap):
    if len(arr) < int(leap):
        return []
    ls = []  # list of indexes that are empty
    for i, spot in enumerate(arr):
        if spot != "":
            ls.append(i)
    ls2 = list(
        range(len(ls) - 1 - int(leap) + 1, -1, -int(leap))
    )  # list of indexes for leap
    return [ls[x] for x in ls2]  # returns list of indexes


def encrypt(plaintext, key):
    # step 1
    ciphertext = ""
    for charac in plaintext:
        if charac in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            ciphertext += charac
    ciphertext = ciphertext.lower()
    ciphertext = ciphertext[::-1]
    ciphertext = [x for x in ciphertext]

    # step 2
    keyNums = []
    for charac in key:
        keyNums.append(str(ord(charac) - 95))

    # step 3
    ls = ["" for x in range(len(ciphertext))]
    right = True
    for keyNum in keyNums:
        # print(ls)
        if right:
            lsindexes = getIndexesRight(ls, keyNum)
            for index in lsindexes:
                ls[index] = ciphertext.pop()
            right = not right
        else:
            lsindexes = getIndexesLeft(ls, keyNum)
            for index in lsindexes:
                ls[index] = ciphertext.pop()
            right = not right
    # find if there are still spaces left
    if "" in ls:
        if right:
            for i in range(len(ls)):
                if ls[i] == "":
                    ls[i] = ciphertext.pop()
        else:
            for i in range(len(ls) - 1, -1, -1):
                if ls[i] == "":
                    ls[i] = ciphertext.pop()

    answer = ""
    for x in ls:
        answer += x
    return answer


def decrypt(ciphertext, key):
    # step 2
    keyNums = []
    for charac in key:
        keyNums.append(str(ord(charac) - 95))
    # print(keyNums)

    # step 3
    ls = [x for x in ciphertext]
    # ls = ["" for x in range(len(ciphertext))]
    right = True
    ans = ""
    for keyNum in keyNums:
        # print(ls)
        # print(ans)
        if right:
            lsindexes = getIndexesRightDecrypt(ls, keyNum)
            for index in lsindexes:
                ans += ls[index]
                ls[index] = ""
            right = not right
        else:
            lsindexes = getIndexesLeftDecrypt(ls, keyNum)
            for index in lsindexes:
                ans += ls[index]
                ls[index] = ""
            right = not right
    # find if there are still spaces left
    flag = True
    for item in ls:
        if item != "":
            flag = False
            break
    if not flag:
        if right:
            for i in range(len(ls)):
                if ls[i] != "":
                    ans += ls[i]
                    ls[i] = ""
        else:
            for i in range(len(ls) - 1, -1, -1):
                if ls[i] != "":
                    ans += ls[i]
                    ls[i] = ""
    return ans


if __name__ == "__main__":
    t, key = input().split()
    text = input()
    if t == "E":
        print(encrypt(text, key))
    elif t == "D":
        print(decrypt(text, key))
