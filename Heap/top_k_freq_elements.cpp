#include <vector>
#include <unordered_map>
#include <queue>
#include <tuple>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        priority_queue<tuple<int, int>> h;
        vector<int> res;

        for(auto num : nums){
            count[num]++;
        }

        for(auto const & [key, val] : count){
            h.push({val, key});
        }

        for(int i = 0; i < k; ++i){
            res.push_back(get<1>(h.top()));
            h.pop();
        }

        return res;
    }
};
