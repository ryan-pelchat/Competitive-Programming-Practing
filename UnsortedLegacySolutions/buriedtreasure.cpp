#include <bits/stdc++.h>
using namespace std;

int main(){
    int numMaps, numLocations;
    cin >> numMaps >> numLocations;
    //vector<unsigned int> maps (numMaps);
    int tempInput, tempInput2;
    map<pair<int, int>, set<pair<bool,bool> > > mapPairs;
    for (int i = 0; i < numMaps; i++){
        cin >> tempInput >> tempInput2;
        if(abs(tempInput) > abs(tempInput2)){
            int tmp = tempInput;
            tempInput = tempInput2;
            tempInput2 = tmp;
        }
        mapPairs[make_pair(abs(tempInput),abs(tempInput2))].insert(make_pair(tempInput>0,tempInput2>0));
        cout << mapPairs[make_pair(abs(tempInput),abs(tempInput2))].size()<<endl;
        if(mapPairs[make_pair(abs(tempInput),abs(tempInput2))].size()>=4){
            cout << "NO";
            exit(0);
        }


    }
    for(auto & i : mapPairs){
        cout << i.first.first << " " <<i.first.second<<" : "<<endl;
        for(auto & j : i.second){
            cout << j.first << " " << j.second << endl;
        }
    }

    cout << "YES";
    // unsigned int temp = 0;
    // temp = (temp << 1) | 1;
    // temp = (temp << 1) | 0;
    // //set nth bit
    // temp = temp|(1<<n);
    // //0001 << n=2 -> 0100 | temp

    // cout << temp;
}
