import collections

customers = int(input())

route = []
dic = {}
for i in range(customers*2):
    r = list(map(int, input().split()))
    if r[0] not in dic.keys():
        dic[r[0]] = [i]
    else:
        dic[r[0]].append(i)
    route.append(r[1])
#print(dic)
#print(route)
totalComplaints = 0
for key in list(dic.keys()):
    templs = []
    #print(key)
    #print(f"{dic[key][0]} \t {dic[key][1]+1}")
    for i in range(dic[key][0], dic[key][1]+1):
        templs.append(route[i])
    #print(templs)
    c = collections.Counter(templs)
    #print(c.most_common())
    for stop in list(c.most_common()):
        #print(stop[1] -1 )
        totalComplaints += stop[1] - 1
print(totalComplaints)
