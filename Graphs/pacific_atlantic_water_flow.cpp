#include <bits/stdc++.h>

using namespace std;

void printContenders(set<pair<int, int>> const & contenders){
    for(auto const & contender : contenders){
        cout << contender.first << ' ' << contender.second << '\n';
    }
}

void printSolution(vector<vector<int>> & vec){
    for(int i = 0; i < vec.size(); i++){
        for(int j = 0; j < vec[0].size(); j++){
            cout << vec[i][j] << ' ';
        }
        cout << '\n';
    }
}

void DFS(vector<vector<int>> const &mat, set<pair<int, int>> & contenders, pair<int, int> coords, int previousHeight){
    if(contenders.count(coords) == 1 || coords.first < 0 || coords.second < 0 || coords.first == mat.size() || coords.second == mat[0].size() || mat[coords.first][coords.second] < previousHeight){
        return;
    }
    contenders.insert(coords);

    DFS(mat, contenders, {coords.first + 1, coords.second}, mat[coords.first][coords.second]);
    DFS(mat, contenders, {coords.first - 1, coords.second}, mat[coords.first][coords.second]);
    DFS(mat, contenders, {coords.first, coords.second + 1}, mat[coords.first][coords.second]);
    DFS(mat, contenders, {coords.first, coords.second - 1}, mat[coords.first][coords.second]);
}

int main(){
    vector<vector<int>> heights = {
        {4,2,7,3,4},
        {7,4,6,4,7},
        {6,3,5,3,6}
    };

    set<pair<int, int>> pacificContenders;
    set<pair<int, int>> atlanticContders;
    vector<vector<int>> intersection;

    int rows = heights.size();
    int cols = heights[0].size();

    for(int i = 0; i < rows; i++){
        DFS(heights, pacificContenders, {i, 0}, heights[i][0]);
    }
    for(int j = 0; j < cols; j++){
        DFS(heights, pacificContenders, {0, j}, heights[0][j]);
    }
    for(int i = 0; i < rows; i++){
        DFS(heights, atlanticContders, {i, cols - 1}, heights[i][cols - 1]);
    }
    for(int j = 0; j < cols; j++){
        DFS(heights, atlanticContders, {rows -1, j}, heights[rows - 1][j]);
    }

    for(auto const & el : pacificContenders){
        if(atlanticContders.count(el) == 1){
            intersection.push_back({el.first, el.second});
        }
    }

    printContenders(pacificContenders);
    printSolution(intersection);

}