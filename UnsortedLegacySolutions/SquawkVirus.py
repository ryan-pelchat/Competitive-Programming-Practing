nodes, edges, infectedStart, t = input().split(" ")

nodes = int(nodes)
edges = int(edges)
infectedStart = int(infectedStart)
time = int(t)

totalSquawks = 0
dic = {}
for i in range(nodes):
    dic[i] = {"nodes": [], "oldS": 0, "newS": 0}
for i in range(edges):
    u, v = input().split(" ")
    u = int(u)
    v = int(v)
    if u not in dic:
        dic[u] = {"nodes": [v], "oldS": 0, "newS": 0}
    else:
        dic[u]["nodes"].append(v)

    if v not in dic:
        dic[v] = {"nodes": [u], "oldS": 0, "newS": 0}
    else:
        dic[v]["nodes"].append(u)

dic[infectedStart]["newS"] = 1

for i in range(time + 1):
    totalSquawks = 0
    for key in list(dic.keys()):  # loop over nodes
        if dic[key]["oldS"] > 0:  # if there are infections to send
            for node in dic[key]["nodes"]:  # loop over neighbors to send infection!
                dic[node]["newS"] += dic[key]["oldS"]
                totalSquawks += dic[key]["oldS"]
    for key in list(dic.keys()):  # loop over nodes
        dic[key]["oldS"] = dic[key]["newS"]
        dic[key]["newS"] = 0
print(totalSquawks)
