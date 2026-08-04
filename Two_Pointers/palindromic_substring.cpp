#include <bits/stdc++.h>

using namespace std;

int countSubstrings(string s) {
    if (s.empty()) return 0;
    
    int count = 0;
    
    for(int i = 0; i < s.size(); ++i){
        int left = i, right = i;
        while(left >= 0 && right < s.size() && s[left] == s[right]){
            count++;
            left--;
            right++;
        }

        left = i;
        right = i + 1;
        while(left >= 0 && right < s.size() && s[left] == s[right]){
            count++;
            left--;
            right++;
        }
    }

    return count;
}

int main(){
    string s = "aaa";
    cout << countSubstrings(s);
}