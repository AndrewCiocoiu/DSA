#include <stdio.h>
#include <stdlib.h>

void DFS(int ** isConnected, int n, int * visited, int u){
    visited[u] = 1;


    for(int i = 0; i < n; i++){
        if(isConnected[u][i] == 1 && !visited[i]){
            DFS(isConnected, n, visited, i);
        }
    }
}


int findCircleNum(int** isConnected, int isConnectedSize, int* isConnectedColSize) {
    int* visited = (int*)calloc(isConnectedSize, sizeof(int));
    int count = 0;

    for(int i = 0; i < isConnectedSize; i++){
        if(!visited[i]){
            DFS(isConnected, isConnectedSize, visited, i);
            count++;
        }
    }
    
    return count;
}

int main(){
    int row0[] = {1, 1, 0};
    int row1[] = {1, 1, 0};
    int row2[] = {0, 0, 1};
    
    int* isConnected[] = {row0, row1, row2};
    int isConnectedColSize = 3;
    printf("%d\n", findCircleNum(isConnected, 3, &isConnectedColSize));
}