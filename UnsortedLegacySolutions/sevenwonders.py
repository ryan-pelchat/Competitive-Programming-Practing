cards = input()

t = cards.count("T")
g = cards.count("G")
c = cards.count("C")

print((t**2 + g**2 + c**2 + 7 * min([t, g, c])))
