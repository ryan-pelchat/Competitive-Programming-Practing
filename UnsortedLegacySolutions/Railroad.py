# https://open.kattis.com/problems/railroad2
junctions, switches = input().split()

junctions = int(junctions)
switches = int(switches)

if switches % 2 == 0 or switches == 0:
    print("possible")
else:
    print("impossible")
