numbers = input()

occurances = [0, 0, 0, 0, 0, 0, 0, 0, 0]
occZero = 0

for number in numbers:
    if number == "0":
        occZero += 1
    else:
        occurances[int(number) - 1] += 1

min_occurances = min(occurances)

if occZero < min_occurances:
    print("1" + "0" * (occZero + 1))
else:  # (common + 1) *
    print((min(occurances) + 1) * str(occurances.index(min_occurances) + 1))
