#include <bits/stdc++.h>
using namespace std;
/*
 * Date: December 14th
 * Problem: The Gourmet
 * Link: https://open.kattis.com/problems/gourmeten
 * Difficulty: 1.8
 * Coder: Ben
 * Editor: Ryan
 * */


long long factorial(int start, int number){
    long long factorial = 1;
    for (int i = start; i <= number; i++) {
        factorial *= i;
    }
    return factorial;
}


int possibilitiesTime (vector<int>  & dishDurations, int totalMinutes, vector<int> & sol, int j){
    if (totalMinutes==0){

        int numOfDishesInSol=0;
        long long divisor =1;
        int maxInt = -1;
        for (auto & i : sol){
            //cout << i << " ";
            if ( i !=0) {
                numOfDishesInSol+=i;
                //divisor*=factorial(i);
                maxInt = max(maxInt,i);
            }
        }
        bool exhaustedMax=false;
        for (auto & i : sol){
            //cout << i << " ";
            if ( i !=0 && (i!=maxInt || exhaustedMax)) {
                //numOfDishesInSol+=i;
                divisor*=factorial(1,i);
            } else if (i == maxInt){
                exhaustedMax=true;
            }
        }
        //cout << endl;
        //cout<< numOfDishesInSol <<endl;
        //n P r
        return factorial(maxInt+1, numOfDishesInSol)/divisor;
    } else if (totalMinutes <0){
        return 0;
    }
    int ret=0;
    for (int i=j; i < dishDurations.size();i++){
        sol[i]++;
        ret+=possibilitiesTime(dishDurations, totalMinutes-dishDurations[i], sol,i);
        sol[i]--;
    }
    return ret;
}


int main() {
    int totalMins, totalDishes;
    cin >> totalMins >> totalDishes;
    vector<int> dishDurations(totalDishes);
    for (int i =0; i < totalDishes;i++){
        cin >> dishDurations[i];
    }
    //int mask = 1 << totalDishes;
    //this will have a bit corresponding to each dish.
    vector<int> sol(totalDishes);
    cout << possibilitiesTime(dishDurations, totalMins, sol,0);

    return 0;
}
