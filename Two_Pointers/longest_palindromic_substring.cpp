#include <bits/stdc++.h>

using namespace std;

string longestPalindrome(string s) {
    if (s.empty()) return "";
    
    string max_str = "";
    
    for(int i = 0; i < s.size(); ++i){
        int left = i, right = i;
        while(left >= 0 && right < s.size() && s[left] == s[right]){
            if ((right - left + 1) > max_str.size()) {
                max_str = s.substr(left, right - left + 1);
            }
            left--;
            right++;
        }

        left = i;
        right = i + 1;
        while(left >= 0 && right < s.size() && s[left] == s[right]){
            if ((right - left + 1) > max_str.size()) {
                max_str = s.substr(left, right - left + 1);
            }
            left--;
            right++;
        }
    }

    return max_str;
}

int main(){
    string s = "cbbd";
    cout << longestPalindrome(s);
}