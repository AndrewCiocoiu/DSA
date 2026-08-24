#include <stdio.h>
#include <stdlib.h>

typedef struct EDGE{
    int s;
    int t;
    int w;
} EDGE;



int parent[100001]; 

int find(int i) {
    return (parent[i] == i) ? i : (parent[i] = find(parent[i]));
}

int sort_by_weight(const void * a, const void * b){
    int aw = ((EDGE*)a)->w;
    int bw = ((EDGE*)b)->w;
    return aw - bw;
}

void print_edges(EDGE edges[], int n){
    for(int i = 0; i < n; i++){
        printf("%d - %d - %d\n", edges[i].s, edges[i].t, edges[i].w);
    }
}


EDGE edges[200001];

int main(){
    int n;
    int m;
    
    FILE *file = fopen("network.txt", "r");

    if(!file){
        perror("Failed to open file");
        exit(0);
    }

    fscanf(file, "%d %d", &n, &m);



    for(int i = 0; i < m; i++){
        int s;
        int t;
        int w;
        fscanf(file, "%d %d %d", &s, &t, &w);


        EDGE new_edge;
        new_edge.s = s;
        new_edge.t = t;
        new_edge.w = w;

        edges[i] = new_edge;
    }

    for (int i = 0; i <= n; i++) {
        parent[i] = i;
    }

    qsort(edges, m, sizeof(EDGE), sort_by_weight);

    int total_cost = 0;
    int count = 0;
    for(int i = 0; i < m && count < n - 1; i++){
        int rootS = find(edges[i].s);
        int rootT = find(edges[i].t);

        if(rootS != rootT){
            count++;
            total_cost += edges[i].w;
            printf("%d --> %d\n", edges[i].s, edges[i].t);
            parent[rootS] = rootT;
        }
    }


    if(count == n - 1){
        printf("Total latency: %d\n", total_cost);
    } else{
        printf("Network disconnected! Impossible to connect!\n");
    }
}