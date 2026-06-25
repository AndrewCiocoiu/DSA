#include <iostream>
#include <vector>

using namespace std;

int missingNumber(vector<int>& nums) {
        int missing_num = 0;
        for(int i = 0; i < nums.size(); i++){
            missing_num = missing_num ^ i ^ nums[i];
        }
        return missing_num ^ nums.size();
}

int main(){
    vector<int> nums = {1, 2, 3};
    cout << missingNumber(nums);
}