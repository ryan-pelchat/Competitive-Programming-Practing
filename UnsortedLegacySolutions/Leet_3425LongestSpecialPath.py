from typing import List

import sys
import json

print(sys.getrecursionlimit())
sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())


class Solution:
    bestPath = [0, 1]  # first is weight, second is number of nodes
    g_adjls = None
    g_nums = None
    g_visitedChildren = set()

    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        # create the adjacency list
        adjls = [[] for _ in range(len(edges) + 1)]

        # index is source, first is destination, second is value
        for edge in edges:
            adjls[edge[0]].append((edge[1], edge[2]))
            adjls[edge[1]].append((edge[0], edge[2]))
        # adjls[edge[1]]

        self.g_adjls = adjls
        self.g_nums = nums
        # print(self.g_adjls)
        # print(self.g_nums)
        # print(self.bestPath)
        self.bestPath = [0, 1]
        self.g_visitedChildren = set()
        self.traverse(0, 0, [0], [nums[0]])
        return self.bestPath

    def traverse(
        self, node: int, weight: int, weightPath: list[int], parentPath: list[int]
    ):
        # we've visited this node now, so remember it
        self.g_visitedChildren.add(node)

        # see if current node makes best path
        if self.bestPath[0] < weight:
            self.bestPath[0] = weight
            self.bestPath[1] = len(parentPath)
            # print(f"Node: {node}\tWeights: {weightPath}")
            # print(f"Node: {node}\tParentPath: {parentPath}")
        elif self.bestPath[0] == weight and self.bestPath[1] > len(parentPath):
            self.bestPath[1] = len(parentPath)
            # print(f"Node: {node}\tWeights: {weightPath}")
            # print(f"Node: {node}\tParentPath: {parentPath}")

        # base case is leaf
        if self.g_adjls[node] == []:
            return None

        # reccursive case
        for child in self.g_adjls[node]:
            if child[0] not in self.g_visitedChildren:
                # determine new path is necessary
                childColour = self.g_nums[child[0]]
                childWeight = child[1]
                newParentPath = parentPath[::]
                newWeight = weightPath[::]
                if childColour in parentPath:
                    # time to chop off path!
                    offendingIndex = parentPath.index(childColour)
                    if offendingIndex == len(parentPath) - 1:
                        newParentPath = [self.g_nums[child[0]]]
                        newWeight = [0]

                    else:
                        newParentPath = newParentPath[offendingIndex + 1 :]
                        newWeight = newWeight[offendingIndex + 2 :]
                        newWeight.insert(0, 0)
                        newParentPath.append(childColour)
                        newWeight.append(childWeight)
                else:
                    newParentPath.append(childColour)
                    newWeight.append(childWeight)

                # search to see if child makes a new path
                # print(f"Node: {node}\tWeights: {weightPath}")
                # print(f"Node: {node}\tParentPath: {parentPath}")

                self.traverse(child[0], sum(newWeight), newWeight, newParentPath)


test = Solution()
print(
    test.longestSpecialPath(
        [[0, 1, 2], [1, 2, 3], [1, 3, 5], [1, 4, 4], [2, 5, 6]], [2, 1, 2, 1, 3, 1]
    )
)
print(test.longestSpecialPath([[1, 0, 8]], [2, 2]))
print(test.longestSpecialPath([[1, 0, 3]], [4, 5]))  # [3,2]

print(
    test.longestSpecialPath(
        [[4, 0, 1], [3, 2, 2], [2, 1, 6], [1, 4, 8]], [3, 2, 3, 4, 1]
    )
)  # [16,4]

print(
    test.longestSpecialPath(
        [[1, 5, 2], [5, 2, 3], [4, 3, 7], [0, 4, 9], [5, 0, 2]], [4, 4, 4, 1, 5, 3]
    )
)  # [16,3]

print(
    test.longestSpecialPath(
        [[0, 1, 2], [1, 2, 3], [1, 3, 5], [1, 4, 4], [2, 5, 6]], [2, 1, 2, 1, 3, 1]
    )
)  # [6,2]

with open("./BenRyan_Practice/Leet_3425LongestSpecialPath.json", "r") as fl:
    data = json.load(fl)

print(test.longestSpecialPath(data[0], data[1]))  # we expect enough memory
