import copy


def rotateMatrix(matrix):
    ansMatrix = copy.deepcopy(matrix)
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            col = len(matrix) - 1 - y
            row = x
            ansMatrix[row][col] = matrix[y][x]
    return ansMatrix


# print(rotateMatrix([[1, 2], [3, 4]]))

matrixSize = input()
matrixSize = int(matrixSize)
# if matrixSize == 0:
#     print("")
#     exit()

grilleInput = []
for x in range(matrixSize):
    grilleInput.append(input())

encryptedString = input()
encryptedString = encryptedString[::-1]
encryptedString = [x for x in encryptedString]

grille = [["" for i in range(matrixSize)] for x in range(matrixSize)]
answerMatrix = [["" for i in range(matrixSize)] for x in range(matrixSize)]
for y in range(matrixSize):
    for x in range(matrixSize):
        grille[y][x] = grilleInput[y][x]

for z in range(4):
    for y in range(matrixSize):
        for x in range(matrixSize):
            if grille[y][x] == ".":
                # answerMatrix[y][x] = grille[y][x]
                if answerMatrix[y][x] == "":
                    answerMatrix[y][x] = encryptedString.pop()
                else:
                    print("invalid grille")
                    exit()
    grille = rotateMatrix(grille)
    # grille = np.rot90(grille, 3)

answer = ""
for y in range(matrixSize):
    for x in range(matrixSize):
        answer += answerMatrix[y][x]

if len(answer) != matrixSize * matrixSize:
    print("invalid grille")
else:
    print(answer)
