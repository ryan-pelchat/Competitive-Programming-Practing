"""
upandaway.py
https://open.kattis.com/problems/upandaway




"""

import heapq

bases, home, firewords = map(int, input().split())
home -= 1

heights = []

for height in map(int, input().split()):
    heights.append(height)

adjList = []

for _ in range(bases):
    adjList.append(map(int, input().split()))

# (distance, firewordsUsed)
distances = [[float("inf"), 0] for _ in range(bases)]

distances[0][0] = 0

pq = []  # priority queue implemeted as a heapqueue

visited = {}

for i in range(bases):
    visited[i] = False

curr = 0  # current location

# visited[0] = True
while visited[home] == False:
    visited[curr] = True
    for i, val in enumerate(adjList[curr]):
        if distances[i][0] > distances[curr][0] + val:
            distances[i][0] = distances[curr][0] + val
            heapq.heappush(pq, (distances[i][0], i))

    while visited[curr] and len(pq) != 0:
        curr = heapq.heappop(pq)[1]


print(distances[home][0])
