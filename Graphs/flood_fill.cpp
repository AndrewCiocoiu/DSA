#include <iostream>
#include <vector>

const std::vector<std::vector<int>> directions{
    {1, 0},
    {-1, 0},
    {0, 1},
    {0, -1}
};

void dfs(int node, std::vector<std::vector<int>>& image, int * visited, int color){
            visited[node] = 1;

            int cols = image[0].size();
            int rows = image.size();

            int r = node / cols;
            int c = node % cols;

            image[r][c] = color;

            for(const auto & dir : directions){
                int new_r = r + dir[0];
                int new_c = c + dir[1];

                if (new_r >= 0 && new_r < rows && new_c >= 0 && new_c < cols && image[new_r][new_c] != 0) {
                    
                    int new_node = new_r * cols + new_c;
                    
                    if(!visited[new_node]){
                        dfs(new_node, image, visited, color);
                    }
                }
            }
        }

int main(){
        std::vector<std::vector<int>> image{
            {1, 1, 1},
            {1, 1, 0},
            {1, 0, 1}
        };


        int adj_size = image.size() * image[0].size();
        int visited[adj_size] = {0};

        int sr = 1;
        int sc = 1;
        int color = 2;

        dfs(image[0].size() * sr + sc, image, visited, color);

        for(int i = 0; i < image.size(); i++){
            for(int j = 0; j < image[0].size(); j++){
                std::cout << image[i][j] << ' ';
            }
            std::cout << '\n';
        }


}