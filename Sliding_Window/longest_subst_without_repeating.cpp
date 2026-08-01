#include <bits/stdc++.h>

using namespace std;

int calculate_window(int left, int right){
    return right - left + 1;
}

int lengthOfLongestSubstring(string s) {
    unordered_map<char, int> char_map;
    int longest_substr = 0;

    int left = 0;
    int right;

    for(right = 0; right < s.size(); right++){
        if(char_map.contains(s[right]) && char_map[s[right]] >= left){
            left = char_map[s[right]] + 1; 
        }

            char_map[s[right]] = right;
            int curr = calculate_window(left, right);
            if(curr > longest_substr){
                longest_substr = curr;
            }
        
    }

    return longest_substr;
}

int main(){
    string s = "pwwkew";
    cout << lengthOfLongestSubstring(s);
}