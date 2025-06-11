#include <bits/stdc++.h>
using namespace std;

bool canBeat(int target,unordered_map<int, vector<int>> &adjList,vector<bool>&visited ,vector<bool>&alive);

int main() {
    int numLeaders, rival, numAlliances;
    cin >> numLeaders >> rival >> numAlliances;
    vector<bool>visited(numLeaders);
    vector<bool>alive(numLeaders,true);
    unordered_map<int, vector<int>> adjList;
    // store alliances in adjList
    int ally1, ally2;

    for (int i = 0; i < numAlliances; i++){
        cin >> ally1 >> ally2;
        adjList[ally1].push_back(ally2);
        adjList[ally2].push_back(ally1);
    }
    if (canBeat(rival, adjList,visited, alive)){
        cout << "NO"<<endl;
    }  else {
        cout <<"YES"<<endl;
    }

}

bool canBeat(int target,unordered_map<int, vector<int>> &adjList,vector<bool>&visited ,vector<bool>&alive){
    visited[target]=true;
    for(int i =0 ;  i < adjList[target].size(); i++){
        if (!visited[adjList[target][i]] && alive[adjList[target][i]]) {
            canBeat(adjList[target][i], adjList, visited, alive);
        }
    }
    int numLivingAllies=0;
    for(int i =0 ;  i < adjList[target].size(); i++){
        if (alive[adjList[target][i]]){
            numLivingAllies++;
        }
    }
    if(numLivingAllies <=1){
        alive[target]=false;
    }
    return alive[target];
}
