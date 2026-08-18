#include <stdio.h>
#include <stdlib.h>

int max(int a, int b){
    if(a > b){
        return a;
    } else {
        return b;
    }
}

int maxProfit(int* prices, int pricesSize) {
    //dp[i][0] || dp[i][1] max profit at the end of day i with eithe share in hand or not
    int dp[10001][2];
    dp[1][0] = 0;
    dp[1][1] = -prices[0];

    for(int i = 2; i <= pricesSize; i++){
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1]);
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i - 1]);
    }

    return dp[pricesSize][0];
}

int main(){
    int prices[10001] = {7,1,5,3,6,4};
    int pricesSize = 6;

    printf("%d\n", maxProfit(prices, pricesSize));
}