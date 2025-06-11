/*
Problem Title: Making a Meowth
Platform: Kattis
Problem URL: https://open.kattis.com/problems/makingameowth
Difficulty: 2.0 - Easy

Driver: Ben
Navigator: Ryan
Date Solved: June 11th 2025
Language: C++

Problem Summary:
    Read P pages with Meowth rereading every Nth page you read. You take X minutes per page, Meowth takes Y minutes per page. How many minutes does it take to read P pages?

Approach:

Represented solution as math equation (y*(p/(n-1)))+x*p

Time Complexity: 0(1)
Space Complexity: 0(1)
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,p,x,y;
    cin >> n >> p >> x >> y;

    cout << (y*(p/(n-1)))+x*p;
    return 0;
}
