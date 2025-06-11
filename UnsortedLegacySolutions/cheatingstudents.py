# https://open.kattis.com/problems/cheatingstudents

# NOT SOLVED :(


numStudents = int(input())

uninfected = set()
for x in range(numStudents):
    uninfected.add(tuple(map(int, input().split())))


def findDistance(coor1: list[int], coor2: list[int]) -> int:
    return (abs(coor1[0] - coor2[0])) + (abs(coor1[1] - coor2[1]))


infected = set()
totalNodes = len(uninfected)
infected.add(uninfected.pop())
totalDistance = 0
while len(infected) < totalNodes:
    # victimList = []
    victimPos = None
    victimMin = 999999999999999999
    for host in infected:
        for victim in uninfected:
            distance = findDistance(host, victim)
            if distance < victimMin:
                victimMin = distance
                # victimList = [victim]
                victimPos = victim
            # elif distance == victimMin:
            #     #victimList.append(victim)
    # for victim in victimList:
    uninfected.remove(victimPos)
    infected.add(victimPos)
    totalDistance += victimMin * 2
print(totalDistance)


# numStudents = int(input())

# uninfected = set()
# for x in range(numStudents):
#     uninfected.add(tuple(map(int, input().split())))


# def findDistance(coor1: list[int], coor2: list[int]) -> int:
#     return (abs(coor1[0] - coor2[0])) + (abs(coor1[1] - coor2[1]))


# # set infected
# # set uninfected
# # {node: [weight, node]}
# for node in uninfected:
#     for node2 in uninfected:
#         pass


# # infected = set()
# # totalNodes = len(uninfected)
# # infected.add(uninfected.pop())
# # totalDistance = 0
# # while len(infected) < totalNodes:
# #     # victimList = []
# #     victimPos = None
# #     victimMin = 999999999999999999
# #     for host in infected:
# #         for victim in uninfected:
# #             distance = findDistance(host, victim)
# #             if distance < victimMin:
# #                 victimMin = distance
# #                 # victimList = [victim]
# #                 victimPos = victim
# #             # elif distance == victimMin:
# #             #     #victimList.append(victim)
# #     # for victim in victimList:
# #     uninfected.remove(victimPos)
# #     infected.add(victimPos)
# #     totalDistance += victimMin * 2
# # print(totalDistance)
