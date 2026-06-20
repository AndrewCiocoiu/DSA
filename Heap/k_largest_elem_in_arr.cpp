#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> maxHeap(nums.begin(), nums.end());
        for(int i = 1; i < k; i++){
            maxHeap.pop();
        }
        return maxHeap.top();
}
int main(){
    vector<int> nums = {3,2,1,5,6,4};
    int k = 2;
    cout << findKthLargest(nums, k);
}