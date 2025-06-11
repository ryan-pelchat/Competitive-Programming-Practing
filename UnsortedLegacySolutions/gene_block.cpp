#include <bits/stdc++.h>
using namespace std;

int main() {
    int testCases;
    cin >> testCases;
    int geneBlock;
    for (int i = 0; i < testCases; i++) {
        cin >> geneBlock;
        switch(geneBlock%10) {
            case 0:
                if(geneBlock < 70) cout << -1;
                else cout << 10;
                break;
            case 1:
                if(geneBlock < 21) cout << -1;
                else cout << 3;
                break;
            case 2:
                if(geneBlock < 42) cout << -1;
                else cout << 6;
                break;
            case 3:
                if(geneBlock < 63) cout << -1;
                else cout << 9;
                break;
            case 4:
                if(geneBlock < 14) cout << -1;
                else cout << 2;
                break;
            case 5:
                if(geneBlock < 35) cout << -1;
                else cout << 5;
                break;
            case 6:
                if(geneBlock < 56) cout << -1;
                else cout << 8;
                break;
            case 7:
                if(geneBlock < 7) cout << -1;
                else cout << 1;
                break;
            case 8:
                if(geneBlock < 28) cout << -1;
                else cout << 4;
                break;
            case 9:
                if(geneBlock < 49) cout << -1;
                else cout << 7;
                break;
        }
        cout << '\n';
    }
    return 0;
}
