/*
Problem Title: Bingo for the Win!
Platform: Kattis
Problem URL: https://open.kattis.com/problems/bingoforthewin
Difficulty: Medium - 3.6
Category: Probability

Driver: Ben
Navigator: Ryan
Date Solved: June 18th 2025
Language: C++

Problem Summary:
    We have a Bingo game between N players who have K squares on their card. Player must fill out all squares to win. Only first player to say they
    have a certain number gets cross of that square. player 1 is faster than 2, player N-1 is faster than player N and so on. We must return the
    probability that each player is the last to complete their card.

Approach:
    Our sample space is the permutation of bingo balls (this is the order). There is one bingo ball per square (with the corresponding number).
    A certain player will lose if the last number in the permutation is a number for which that player is the slowest with that number. We add the
    percentages of all the permutations for which that player loses to determine the total probability of that player losing.

Time Complexity: 0(N*K)
Space Complexity: 0(N*K)

*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    bool debug = false;

    cin >> n >>k;

    //n bingo cards of size k
    vector<vector<int>> bingoCards (n, vector<int>(k));


    // loop over n bingo cards
    for (int i = 0; i < n; i++) {
        //loop over j numbers in card
        for (int j = 0; j < k; j++) {
            cin >> bingoCards[i][j];
        }
    }
    if (debug) {
        for (int i = 0; i < n; i++) {
            //loop over j numbers in card
            for (int j = 0; j < k; j++) {
                cout << bingoCards[i][j];
            }
        }
    }


    //backwards entries
    unordered_map<int,int> uniqueNumbers;
    // amount numbers for which this bingo card the last of
    vector<int> numOfUniqueNumbers(n);
    for (int i = n - 1; i >= 0; i--) {
        //loop over j numbers in card
        for (int j = 0; j < k; j++) {

            uniqueNumbers[bingoCards[i][j]]++;
            if (uniqueNumbers[bingoCards[i][j]] == 1) {
                bingoCards[i][j]*=-1;
            }

        }
    }
    double prob=0;
    for (int i = 0; i < n; i++) {
        prob=0;
        for (int j=0; j < k;j++){
            if (bingoCards[i][j]<0){
                prob+=(double)uniqueNumbers[bingoCards[i][j]*-1]/(double)(n*k);
            }
        }
        cout << prob<<endl;
    }




    return 0;
}
