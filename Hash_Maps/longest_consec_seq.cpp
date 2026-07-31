#include <bits/stdc++.h>

using namespace std;

int longestConsecutive(vector<int>& nums) {
        unordered_set<int> n;
        n.insert_range(nums);

        int max_seq = 0;

        for(auto const & num : nums){
            int curr_seq = 1;
            if(!n.count(num - 1)){
                int i = num;
                while(n.count(i + 1)){
                    curr_seq++;
                    i++;
                }
                if(curr_seq > max_seq){
                    max_seq = curr_seq;
                }
            }
        }

        return max_seq;
}

int main(){
    vector<int> nums = {100,4,200,1,3,2};

    cout << longestConsecutive(nums);
}