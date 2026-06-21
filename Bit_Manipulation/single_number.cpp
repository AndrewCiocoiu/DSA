#include <iostream>
#include <vector>

using namespace std;

int singleNumber(vector<int>& nums) {
    int curr = nums[0];
    for(auto i = 1; i < nums.size(); i++){
        curr = curr ^ nums[i];
    }
    return curr;
        
}

int main(){
    vector<int> nums = {2, 2, 1};
    cout << singleNumber(nums);

}