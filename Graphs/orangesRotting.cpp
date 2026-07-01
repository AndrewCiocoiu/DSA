#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int BFS(vector<vector<int>> &grid, int r, int c){
    queue<pair<int, int>> q;

    int rows = grid.size();
    int cols = grid[0].size();

    q.push({r, c});
    grid[r][c] = 0;

    int distance = 0;

    vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    while(!q.empty()){
        int qSize = q.size();
        for(int i = 0; i < qSize; i++){

            auto exploredNode = q.front();
            q.pop();

            for(auto const & dir : directions){
                int newR = exploredNode.first + dir.first;
                int newC = exploredNode.second + dir.second;

                if(newR >= rows || newC >= cols || newR < 0 || newC < 0 || grid[newR][newC] != 1){
                    continue;
                }

                q.push({newR, newC});
                grid[newR][newC] = 0;
            }
        }

        distance++;
    }

    return distance - 1;
}

int orangesRotting(vector<vector<int>>& grid) {
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[0].size(); j++){
                if(grid[i][j] == 2){
                    int distance = BFS(grid, i, j);
                    for(int k = i; k < grid.size(); k++){
                        for(int l = j; l < grid[0].size(); l++){
                            if(grid[k][l] == 1){
                                return -1;
                            }
                        }
                    }
                    return distance;
                }
            }
        }
}

int main(){
    vector<vector<int>> grid = {{2,1,1},{1,1,0},{0,1,1}};
    cout << orangesRotting(grid) << '\n';
}