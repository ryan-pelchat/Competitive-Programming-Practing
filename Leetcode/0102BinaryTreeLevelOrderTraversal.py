"""
Problem Title: 102. Binary Tree Level Order Traversal
Platform: Leetcode
Problem URL: https://leetcode.com/problems/binary-tree-level-order-traversal
Difficulty: Medium
Category: Tree, Breadth-First Search, Binary Tree

Driver: Ryan
Navigator: Ben
Date Solved: 2025-08-29
Language: Python3

Problem Summary:
    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

    Example 1:

    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

    Example 2:

    Input: root = [1]
    Output: [[1]]

    Example 3:

    Input: root = []
    Output: []


    Constraints:

        The number of nodes in the tree is in the range [0, 2000].
        -1000 <= Node.val <= 1000



Approach:
    - strategy
        - recurse into each children while keeping track of depth and
          values that we come across
        - append to a list when we reached a new depth
        - extend to the proper depth when traversing a depth we already
          visited
    - technique (two pointers, recursion, BFS, etc...)
        - recursion
    - why did you choose it?
        - problems with trees are easier to solve using recursion
    - edge cases considered?
        - should the root level be depth 1 or 0? (it should be 1)

Time Complexity: 0(N)
Space Complexity: 0(N)

Notes:
"""

from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Some Test Cases:

Input:
    [0,2,4,1,null,3,-1,5,1,null,6,null,8]
Expected:
    [[0],[2,4],[1,3,-1],[5,1,6,8]]
"""


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        return self.levelOrderTraversal(root, [[root.val]], 1)

    def levelOrderTraversal(
        self, root: TreeNode, arr: List[List[int]], depth: int
    ) -> List[List[int]]:
        if root is None:
            return arr

        currentLevel = []

        if root.left is not None:
            currentLevel.append(root.left.val)
        if root.right is not None:
            currentLevel.append(root.right.val)

        if len(currentLevel) != 0:
            # if true, then we are at the end of the tree!!
            # so no extending/appending
            if depth < len(arr):
                arr[depth].extend(currentLevel)
            else:
                arr.append(currentLevel)
        # if root.left is not None and root.right is not None:
        #     print(f"root.left: {str(root.left.val)}\t root.right: {str(root.right.val)}\t level: {depth}")
        # elif root.left is None and root.right is not None:
        #     print(f"root.left: NONE\t root.right: {str(root.right.val)}\t level: {depth}")
        # elif root.left is not None and root.right is None:
        #     print(f"root.left: {str(root.left.val)}\t root.right: NONE\tlevel: {depth}")
        # else:
        #     print(f"root.left: NONE\t root.right: NONE\tlevel: {depth}")
        if root.left is not None:
            self.levelOrderTraversal(root.left, arr, depth + 1)
        if root.right is not None:
            self.levelOrderTraversal(root.right, arr, depth + 1)

        return arr

        # [3,9,20,3,4,15,7]
