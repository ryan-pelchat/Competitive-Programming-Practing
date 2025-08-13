/*
Problem Title: 3644. Maximum K to Sort a Permutation
Platform: LeetCode
Problem URL: https://leetcode.com/problems/maximum-k-to-sort-a-permutation/
Difficulty: Medium
Category: Contest 462

Driver: Ben
Navigator: Ryan
Date Solved: 2025-08-13
Language: C++

Problem Summary:
You are given an integer array nums of length n, where nums is a permutation of the numbers in the range [0..n - 1].

You may swap elements at indices i and j only if nums[i] AND nums[j] == k, where AND denotes the bitwise AND operation and k is a non-negative integer.

Return the maximum value of k such that the array can be sorted in non-decreasing order using any number of such swaps. If nums is already sorted, return 0.

Approach:
    We found all of the numbers in the permutation that were out of place. We bitwise anded them all together to get the biggest number K that allows us to swap the out of place numbers.

Time Complexity: 0(n)
Space Complexity: 0(n)

Notes:
*/

class Solution {
public:
    int sortPermutation(vector<int>& nums) {
        vector<int> outOfPlace;
        for (int index =0; index < nums.size(); index++){
            if (nums[index]!=index){
                outOfPlace.push_back(nums[index]);
            }
        }
        int ret=0;
        /*for (int i =0 ; i < outOfPlace.size();i++){
            cout << outOfPlace[i]<<" ";
        }*/
        cout << endl;
        if (outOfPlace.size()>0){
            ret=outOfPlace[0];
            for (int i =1 ; i < outOfPlace.size();i++){
                ret=ret & outOfPlace[i];
                //cout << "ret : "<< ret<<endl;
            }
        }
        //cout << "ret before submit : " << ret;
        return ret;
    }
};