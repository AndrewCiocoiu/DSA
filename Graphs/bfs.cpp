#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void BFS(vector<vector<int>>& grid, int r, int c){
    int rows = grid.size();
    int cols = grid[0].size();

    queue<pair<int, int>> q;

    q.push({r, c});
    grid[r][c] = 0;

    vector<pair<int, int>> directions = {
        {-1, 0}, {1, 0}, {0, -1}, {0, 1}
    };

    while(!q.empty()){
        auto [r_curr, c_curr] = q.front();
        q.pop();
    }

    for(const auto& dir : directions){
        int new_r = dir.first;
        int new_c = dir.second;

        if (new_r >= 0 && new_r < rows && new_c >= 0 && new_c < cols) {
                if (grid[new_r][new_c] != 0 && grid[new_r][new_c] != -1) {
                    q.push({new_r, new_c});
                    grid[new_r][new_c] = 0;
                }
        }
    }
}

void islandsAndTreasure(vector<vector<int>>& grid) {
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[0].size(); j++){
                if (grid[i][j] != 0 && grid[i][j] != -1){
                    BFS(grid, i, j);
                }
            }
        }
}

void printGrid(vector<vector<int>> const &grid){
    for(int i = 0; i < grid.size(); i++){
        for(int j = 0; j < grid[0].size(); j++){
            cout << grid[i][j] << ' ';
        }
        cout << '\n';
    }
}

int main(){
    vector<vector<int>> grid = {
        {2147483647,-1,0,2147483647},
        {2147483647,2147483647,2147483647,-1},
        {2147483647,-1,2147483647,-1},
        {0,-1,2147483647,2147483647}
    };
    islandsAndTreasure(grid);
    printGrid(grid);
}