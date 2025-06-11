cornVals = list(map(int, input().split()))
rows, kwf = map(int, input().split())
totAvg = 0
for x in range(0,len(cornVals), 2):
    totAvg += cornVals[x]*cornVals[x+1]

totAvg = totAvg//5

print(rows*totAvg//kwf)