#include <iostream>
#include <vector>

using namespace std;

int DFS(int r, int c, vector<vector<int>> &mat){
    int rows = mat.size();
    int col = mat[0].size();

    if(r < 0 || c < 0 || r >= rows || c >= col){
        return 0;
    }

    if(mat[r][c] == 0){
        return 0;
    }

    mat[r][c] = 0;

    return 1 + DFS(r + 1, c, mat)
    + DFS(r - 1, c, mat)
    + DFS(r, c + 1, mat)
    + DFS(r, c - 1, mat);

}

int maxAreaOfIsland(vector<vector<int>>& grid) {
    int maxCount = 0;

    for(int i = 0; i < grid.size(); i++){
        for(int j = 0; j < grid[0].size(); j++){
            if(grid[i][j] == 1){
                int currentCount = DFS(i, j, grid);
                if(currentCount > maxCount){
                    maxCount = currentCount;
                }
            }
        }
    }
    return maxCount;
}

int main(){
    vector<vector<int>> grid = {
        {0,1,1,0,1},
        {1,0,1,0,1},
        {0,1,1,0,1},
        {0,1,0,0,1}
    };

    cout << maxAreaOfIsland(grid);
}