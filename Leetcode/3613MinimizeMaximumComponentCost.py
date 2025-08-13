"""
Problem Title: 3613. Minimize Maximum Component Cost
Platform: Leetcode
Problem URL: https://leetcode.com/problems/minimize-maximum-component-cost
Difficulty: Medium
Category: Binary Search, Sort, Union Find, Graph

Driver: Ryan
Navigator: Ben
Date Solved: 2025-07-16
Language: Python3

Problem Summary:
    You are given an undirected connected graph with n nodes labeled from
    0 to n - 1 and a 2D integer array edges where edges[i] = [ui, vi, wi]
    denotes an undirected edge between node ui and node vi with weight wi,
    and an integer k.

    You are allowed to remove any number of edges from the graph such that
    the resulting graph has at most k connected components.

    The cost of a component is defined as the maximum edge weight in that
    component. If a component has no edges, its cost is 0.

    Return the minimum possible value of the maximum cost among all components
    after such removals.

Approach:
    - Create a Minimum Spanning Tree using a variation of the Kruskal algorith
        - variation is that we use an array with pointers to act as union mergers
        - the index of the array is the name of the node
        - the value at index in array is the name of the parent node
        - when merging, change parent node to point to new parent

Time Complexity: 0(...)
Space Complexity: 0(...)

Notes:
    -
"""

import heapq
from typing import *


class Solution:

    def find(self, pointedArray: List[int], x: int) -> int:
        if pointedArray[x] == x:
            return x
        else:
            return self.find(pointedArray, pointedArray[x])

    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        pointerArray = [x for x in range(n)]
        edgesKept = []
        sortedEdgeList = sorted(edges, key=lambda x: edges[2], reverse=True)
        maxWeight = 9999999999
        for edge in sortedEdgeList:
            edge0parent = self.find(pointerArray, edge[0])
            edge1parent = self.find(pointerArray, edge[1])

            if edge0parent != edge1parent:
                if edge0parent < edge1parent:
                    pointerArray[edge1parent] = edge0parent
                else:
                    pointerArray[edge0parent] = edge1parent
                heapq.heappush(edgesKept, (edge[2], edge[0], edge[1]))

        return heapq.nlargest(k, edgesKept)[-1][0]


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.minCost(
            7,
            [
                [0, 1, 4],
                [1, 2, 3],
                [1, 3, 2],
                [3, 4, 6],
                [1, 5, 3],
                [4, 6, 5],
            ],
            2,
        )
    )

"""
# 1. find loops, cut the heaviest edge
# 2. cut k-1 heaviest edges 
# 3. return
import heapq
class Solution:
    
    def find(self, pointedArray: List[int], x:int) -> int:
        if pointedArray[x]==x:
            return x
        else:
            return self.find(pointedArray, pointedArray[x])
    
    
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        pointerArray = [x for x in range(n)]
        edgesKept = []
        sortedEdgeList = sorted(edges, key=lambda x : edges[2], reverse=True)
        maxWeight = 9999999999
        for edge in sortedEdgeList:
            edge0parent=self.find(pointerArray,edge[0])
            edge1parent=self.find(pointerArray, edge[1])
            
            if edge0parent != edge1parent:
                if edge0parent < edge1parent:
                    pointerArray[edge1parent] = edge0parent
                else:
                    pointerArray[edge0parent] = edge1parent
                heapq.heappush(edgesKept, edge[2])
        return heapq.nlargest(k, edgesKept)[-1]
"""
