#include <unordered_map>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        vector<vector<string>> res;

        for(const auto & s : strs){
            string ordered_copy = s;

            sort(ordered_copy.begin(), ordered_copy.end());

            groups[ordered_copy].push_back(s);
        } 

        for(const auto & [key, val] : groups){
            res.push_back(val);
        }

        return res;
    }
};
