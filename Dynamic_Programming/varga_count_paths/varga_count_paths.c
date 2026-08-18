#include <stdio.h>
#include <stdlib.h>

typedef struct EDGE{
    int src;
    int dest;
} EDGE;

void print_edges(EDGE * edges, int k){
    for(int i = 0; i < k; i++){
        printf("%d %d\n", edges[i].src, edges[i].dest);
    }
}

int main(){
    FILE *file = fopen("graph.txt", "r");

    if(!file){
        perror("Failed to open file!");
        exit(0);
    }

    int node_nr;
    int edge_nr;

    int k;
    int s;

    fscanf(file, "%d %d", &node_nr, &edge_nr);


    EDGE * edges = calloc(101, sizeof(EDGE));

    for(int i = 0; i < edge_nr; i++){
        int src;
        int dest;
        fscanf(file, "%d %d", &src, &dest);

        edges[i].src = src;
        edges[i].dest = dest;
    }

    fscanf(file, "%d %d", &k, &s);
    fclose(file);


    long long dp[101][101] = {0};
    dp[0][s] = 1;

    for(int step = 1; step <= k; step++){
        for(int curr_edge = 0; curr_edge < edge_nr; curr_edge++){
            int s = edges[curr_edge].src;
            int d = edges[curr_edge].dest;

            dp[step][d] += dp[step - 1][s];
        }
        
    }


    long long total_paths = 0;
    for(int i = 1; i <= node_nr; i++){
        total_paths += dp[k][i];
    }

    printf("%lld", total_paths);
    
}