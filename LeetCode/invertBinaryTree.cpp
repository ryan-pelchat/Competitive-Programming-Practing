/*
Problem Title: Invert Binary Tree
Platform: Leetcode
Problem URL: https://leetcode.com/problems/invert-binary-tree/description
Difficulty: Easy
Category: Trees

Driver: Ben
Navigator: Ryan
Date Solved: August 29th 2025
Language: C++ 

Problem Summary:
    Flip the left and right nodes of a binary tree

Approach:
    - strategy
        Go through the tree and make the left node the right node and the right node the left node
    - technique (two pointers, recursion, BFS, etc...)
        Recursion was used.
    - why did you choose it?
        It allowed us to do this process for all nodes since the recursive method is guarenteed to reach all nodes
    - edge cases considered?
        When the recrusive function is asked to recurse on a null pointer (we just return the null pointer)

Time Complexity: 0(N) where N is number of nodes
Space Complexity: 0(N)

Notes:
*/
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
    public:
        TreeNode* invertTree(TreeNode* root) {
            if (!root) return root;
            TreeNode* tmp = invertTree(root-> left);
            root->left =invertTree(root->right);
            root->right=tmp;
            return root;
        }
};