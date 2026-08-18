#include <stdio.h>
#include <stdlib.h>


int min(int a, int b){
    if(a < b){
        return a;
    } else {
        return b;
    }
}

int minCostClimbingStairs(int* cost, int costSize) {
    

    
    //state: minimum cost to reach step i
    int dp[costSize + 1];

    //base case: I can take either 0 or 1 for free
    dp[0] = 0;
    dp[1] = 0;

    for(int i = 2; i <= costSize; i++){
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
    }

    return dp[costSize];

}

int main(){
    int cost[1001] = {10, 15, 20};
    int costSize = 3;

    printf("%d", minCostClimbingStairs(cost, costSize));

}