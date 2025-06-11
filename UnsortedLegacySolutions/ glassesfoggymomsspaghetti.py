import math


d, x, y, h = map(int, input().split())

bigTriangleAngle = math.atan((y + h / 2) / x)
mediumTriangleAngle = math.atan(y / x)
smallTriangleAngle = math.atan((y - (h / 2)) / x)
a_smallAngle = bigTriangleAngle - mediumTriangleAngle
b_smallAngle = bigTriangleAngle - (smallTriangleAngle + a_smallAngle)

ap_sideLength = math.tan(a_smallAngle) * d
bp_sideLength = math.tan(b_smallAngle) * d

print(ap_sideLength + bp_sideLength)
