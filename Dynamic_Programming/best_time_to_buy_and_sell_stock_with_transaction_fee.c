#include <stdio.h>
#include <stdlib.h>

int max(int a, int b){
    if(a > b){
        return a;
    } else {
        return b;
    }
}

int maxProfit(int* prices, int pricesSize, int fee) {
    int dp[50001][2];
    dp[0][0] = 0;
    dp[0][1] = -prices[0];

    for(int i = 1; i < pricesSize; i++){
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + (prices[i] - fee));
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] ); 
    }

    return dp[pricesSize - 1][0];

}

int main(){
    int prices[50001] = {1,3,2,8,4,9};
    int fee = 2;
    printf("%d\n", maxProfit(prices, 6, fee));
}