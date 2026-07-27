#include <bits/stdc++.h>

using namespace std;


void BFS(vector<vector<char>> & board, unordered_set<int> & visited, int r, int c){
    int rows = board.size();
    int cols = board[0].size();
    vector<pair<int, int>> group;
    int valid = true;
    queue<pair<int, int>> q;

    q.push({r, c});
    visited.insert(r * cols + c);
    group.push_back({r, c});

    vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    while(!q.empty()){
        pair<int, int> curr = q.front();
        q.pop();

        for(auto const & dir : directions){
            pair<int, int> explored = {dir.first + curr.first, dir.second + curr.second};
            if(explored.first == rows || explored.first < 0 || explored.second == cols || explored.second < 0){
                valid = false;
                continue;
            }
            if(board[explored.first][explored.second] == 'X' || visited.count(cols * explored.first + explored.second) == 1){
                continue;
            }
            q.push({explored.first, explored.second});
            visited.insert(cols * explored.first + explored.second);
            group.push_back({explored.first, explored.second});
        }
    }

    if(valid){
        for(auto const & item : group){
            board[item.first][item.second] = 'X';
        }
    }
}

void solve(vector<vector<char>>& board) {

        unordered_set<int> visited;

        for(int i = 0; i < board.size(); i++){
            for(int j = 0; j < board[0].size(); j++){
                if(board[i][j] == 'O' && visited.count(i * board[0].size() + j) == 0){
                    BFS(board, visited, i, j);
                }
            }
        }
}

void printBoard(vector<vector<char>> const & board){
    for(int i = 0; i < board.size(); i++){
        for(int j = 0; j < board[0].size(); j++){
            cout << board[i][j] << ' ';
        }
        cout << '\n';
    }
}

int main(){
    vector<vector<char>> board = {
        {'X','X','X','X'},
        {'X','O','O','X'},
        {'X','X','O','X'},
        {'X','O','X','X'}
    };

    solve(board);
    printBoard(board);
}