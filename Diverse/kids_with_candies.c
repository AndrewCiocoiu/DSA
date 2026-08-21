/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize) {
    int max = -1;
    for(int i = 0; i < candiesSize; i++){
        if(candies[i] > max){
            max = candies[i];
        }
    }
    
    bool * res = calloc(candiesSize, sizeof(bool));

    for(int i = 0; i < candiesSize; i++){
        if(candies[i] + extraCandies >= max){
            res[i] = true;
        }
    }
    *returnSize = candiesSize;

    return res;
}