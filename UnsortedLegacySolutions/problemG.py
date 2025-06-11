expression = input()

temp = expression.split("=")
if eval(temp[0]) == int(temp[1]):
    print(expression)

expression = expression.split(" ")

indexOuter = 0
for digit in expression[0][0 : len(expression[0]) - 1]:
    indexInner = 0
    for digit2 in expression[4][0 : len(expression[4]) - 1]:
        # total2 += digit2

        newNum = int(expression[4][: indexInner + 1] + expression[0][indexOuter + 1 :])
        newNum2 = int(expression[0][: indexOuter + 1] + expression[4][indexInner + 1 :])
        if expression[1] == "+":
            if newNum + int(expression[2]) == newNum2:
                print(
                    str(newNum)
                    + " "
                    + expression[1]
                    + " "
                    + (expression[2])
                    + " = "
                    + str(newNum2)
                )
                break
        else:
            if newNum * int(expression[2]) == newNum2:
                print(
                    str(newNum)
                    + " "
                    + expression[1]
                    + " "
                    + (expression[2])
                    + " = "
                    + str(newNum2)
                )
                break
        indexInner += 1
    indexOuter += 1

indexOuter = 0
for digit in expression[0][0 : len(expression[0]) - 1]:
    indexInner = 0
    for digit2 in expression[2][0 : len(expression[2]) - 1]:
        # total2 += digit2

        newNum = int(expression[2][: indexInner + 1] + expression[0][indexOuter + 1 :])
        newNum2 = int(expression[0][: indexOuter + 1] + expression[2][indexInner + 1 :])
        if expression[1] == "+":
            if newNum + newNum2 == int(expression[4]):
                print(
                    str(newNum)
                    + " "
                    + expression[1]
                    + " "
                    + str(newNum2)
                    + " = "
                    + expression[4]
                )
                break
        else:
            if newNum * newNum2 == int(expression[4]):
                print(
                    str(newNum)
                    + " "
                    + expression[1]
                    + " "
                    + str(newNum2)
                    + " = "
                    + expression[4]
                )
                break
        indexInner += 1
    indexOuter += 1

indexOuter = 0
for digit in expression[2][0 : len(expression[2]) - 1]:
    indexInner = 0
    for digit2 in expression[4][0 : len(expression[4]) - 1]:
        # total2 += digit2

        newNum = int(expression[4][: indexInner + 1] + expression[2][indexOuter + 1 :])
        newNum2 = int(expression[2][: indexOuter + 1] + expression[4][indexInner + 1 :])
        if expression[1] == "+":
            if int(expression[0]) + newNum == newNum2:
                print(
                    expression[0]
                    + " "
                    + expression[1]
                    + " "
                    + str(newNum)
                    + " = "
                    + str(newNum2)
                )
                break
        else:
            if int(expression[0]) * newNum == newNum2:
                print(
                    expression[0]
                    + " "
                    + expression[1]
                    + " "
                    + str(newNum)
                    + " = "
                    + str(newNum2)
                )
                break
        indexInner += 1
    indexOuter += 1
