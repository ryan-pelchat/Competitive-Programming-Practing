/*
 * date: March 22nd 2025
 * Authors: Ben and Ryan
 * Problem: https://open.kattis.com/problems/cheatingstudents*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    bool debug=false;
    int amount;
    cin  >> amount;
    // mapping key to coords
    vector<pair<int,int>>map(amount);
    // [0] -> key : 0 , [1] ->
    vector<vector<int>> adjList(amount, vector<int>(amount));
    vector<bool> visited(amount,false);
    //priority first= distance second = destination
    priority_queue<pair<int,int>, vector<pair<int,int>> , greater<pair<int,int>>> pq;
    int x,y;
    for (int i = 0; i <  amount; i++){
        cin >> x >> y;
        map[i]=make_pair(x,y);
    }
    for (int i = 0; i <  amount; i++){
        for (int j = 0; j <  amount; j++){
            adjList[i][j]=abs(map[i].first-map[j].first)+abs(map[i].second-map[j].second);
        }
    }
    int curr=0;
    int nodesVisited=0;
    int toAddToDistance;
    int totalDistance=0;
    while (nodesVisited+1 < amount){
        if (debug) cout << "in new loop, the curr is "<<curr<<endl;
        visited[curr]=true;
        nodesVisited++;
        for(int i = 0; i < amount;i++){
            if (!visited[i]){
                pq.push(make_pair(adjList[curr][i],i));
            }
        }
        do {

            curr= pq.top().second;
            toAddToDistance= pq.top().first;
            if (debug) cout << "curr "<< curr<<endl;
            if (debug) cout << "visited " <<visited[curr]<<endl;
            if (debug) cout << "pq size " <<pq.size()<<endl;
            pq.pop();
        } while (visited[curr]);
        totalDistance+=toAddToDistance;
        if (debug) cout << "total distance " << totalDistance<<endl;
    }
    cout << totalDistance*2;
    return 0;
}
