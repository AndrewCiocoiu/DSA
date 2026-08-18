#include <stdio.h>
#include <stdlib.h>

int max(int a, int b){
    if(a > b){
        return a;
    } else {
        return b;
    }
}

int rob(int* nums, int numsSize) {

    if(numsSize == 1){
        return nums[0];
    }
    //dp[i] the max I can rob from the first i houses
    int dp[numsSize];
    dp[0] = nums[0];
    dp[1] = max(nums[0], nums[1]);

    for(int i = 2; i < numsSize; i++){
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]);
    }

    return dp[numsSize - 1];


}

int main(){
    int nums[101] = {2,7,9,3,1};
    int numsSize = 5;

    printf("%d\n", rob(nums, numsSize));
}