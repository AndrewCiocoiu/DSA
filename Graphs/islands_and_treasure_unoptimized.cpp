#include <iostream>
#include <vector>
#include <queue>

#define INF 2147483647

using namespace std;

int BFS(vector<vector<int>> &grid, int r, int c){
    queue<pair<pair<int, int>, int>> q;

    int rows = grid.size();
    int cols = grid[0].size();

    vector<bool> visited(rows * cols, false);

    q.push({{r, c}, 0});
    visited[r * cols + c] = true;

    vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1,0}, {-1, 0}};

    while(!q.empty()){
        auto [coords, distance] = q.front();
        auto [row, col] = coords;
        q.pop();

        if(grid[row][col] == 0){
            return distance;
        }

        for(auto const & dir : directions){
            auto new_r = row + dir.first;
            auto new_c = col + dir.second;
            
            if(new_r >= rows || new_r < 0 || new_c >= cols || new_c < 0){
                continue;
            }

            if((grid[new_r][new_c] == INF || grid[new_r][new_c] == 0) && !visited[new_r * cols + new_c]){
                visited[new_r * cols + new_c] = true;
                q.push({{new_r, new_c}, distance + 1});
            }
        }
    }

    return INF;
}

void islandsAndTreasure(vector<vector<int>>& grid) {
    for(auto i = 0; i < grid.size(); i++){
        for(auto j = 0; j < grid[0].size(); j++){
            if(grid[i][j] == INF){
                int distance = BFS(grid, i, j);
                grid[i][j] = distance;
            }
        }
    }    
}

void showGrid(vector<vector<int>> const &grid){
    for(auto i = 0; i < grid.size(); i++){
        for(auto j = 0; j < grid[0].size(); j++){
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
        {0,-1,2147483647,2147483647}};
    
        islandsAndTreasure(grid);

    showGrid(grid);
}