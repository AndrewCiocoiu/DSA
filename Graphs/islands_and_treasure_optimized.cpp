#include <iostream>
#include <vector>
#include <queue>

using namespace std;

typedef struct point{
    int r;
    int c;
    int distance;
} point;

void BFS(vector<vector<int>> &grid){
    int rows = grid.size();
    int cols = grid[0].size();

    queue<point> q;
    
    for(auto r = 0; r < rows; r++){
        for(auto c = 0; c < cols; c++){
            if(grid[r][c] == 0){
                q.push({r, c, 0});
            }
        }
    }

    vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    while(!q.empty()){
        point current_point = q.front();
        q.pop();

        for(auto i = 0; i < 4; i++){
            int new_r = current_point.r + directions[i].first;
            int new_c = current_point.c + directions[i].second;
            int new_size = current_point.distance + 1;

            point new_point = {new_r, new_c, new_size};

            if (new_r < 0 || new_r >= rows || new_c < 0 || new_c >= cols || grid[new_r][new_c] <= new_size) {
                continue;
            }

            q.push(new_point);
            grid[new_r][new_c] = new_size;
        
        }
    }
}

void islandsAndTreasure(vector<vector<int>> &grid){
    BFS(grid);
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