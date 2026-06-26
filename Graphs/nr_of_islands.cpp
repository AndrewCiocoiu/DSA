#include <iostream>
#include <vector>

using namespace std;

void DFS(int r, int c, vector<vector<char>> &mat){
    int rows = mat.size();
    int col = mat[0].size();

    if(r < 0 || c < 0 || r >= rows || c >= col){
        return;
    }

    if(mat[r][c] == '0'){
        return;
    }

    mat[r][c] = '0';
    DFS(r + 1, c, mat);
    DFS(r - 1, c, mat);
    DFS(r, c + 1, mat);
    DFS(r, c - 1, mat);
}

int numIslands(vector<vector<char>>& grid) {
        int isle_count = 0;
        for(int i = 0; i < grid.size();i++){
            for(int j = 0; j < grid[0].size(); j++){
                if(grid[i][j] == '1'){
                    isle_count++;
                    DFS(i, j, grid);
                }
            }
        }
        return isle_count;
}

int main(){
    vector<vector<char>> grid = {
        {'1','1','0','0','0'},
        {'1','1','0','0','0'},
        {'0','0','1','0','0'},
        {'0','0','0','1','1'}
    };

    cout << numIslands(grid);
}