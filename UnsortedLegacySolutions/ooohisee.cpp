#include <bits/stdc++.h>
using namespace std;

bool checkSquare(vector<vector<char>> &grid, int row, int col){
    if (grid[row][col]=='0') {
        if (grid[row - 1][col - 1] == 'O' && grid[row][col - 1] == 'O' && grid[row + 1][col - 1] == 'O' &&
            grid[row - 1][col] == 'O' && grid[row + 1][col] == 'O' &&
            grid[row - 1][col + 1] == 'O' && grid[row][col + 1] == 'O' && grid[row + 1][col + 1] == 'O') {
            return true;
        }
    }
    return false;
}


int main() {
    int rows, cols;
    cin >> rows >> cols;
    cin.ignore(256,'\n');
    vector<vector<char>> grid(rows,vector<char>(cols));
    for (int rowsIn =0; rowsIn < rows;rowsIn++){
        for (int colsIn = 0; colsIn <cols; colsIn++){
            scanf("%c",&grid[rowsIn][colsIn]);
        }
        cin.ignore(256,'\n');
    }

    int locations=0;
    int outputRow;
    int outputCol;
    for (int rowsGo =1; rowsGo<rows-1;rowsGo++){
        for (int colsGo=1; colsGo<cols-1;colsGo++){
            if (checkSquare(grid, rowsGo, colsGo)){
                if (locations==0){
                    outputRow = rowsGo;
                    outputCol=colsGo;
                }
                locations++;
            }
        }
    }

    if (locations ==0){
        cout << "Oh no!";
    } else if (locations == 1){
        cout << outputRow+1 << " " << outputCol+1;
    } else {
        cout << "Oh no! " << locations << " locations";
    }
    return 0;
}
