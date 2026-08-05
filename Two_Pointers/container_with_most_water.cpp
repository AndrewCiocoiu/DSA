#include <bits/stdc++.h>

using namespace std;

int maxArea(vector<int>& height) {
    int left = 0;
    int right = height.size() - 1;

    int max_height = 0;

    while(left < right){
        if(min(height[left], height[right]) * (right - left) > max_height){
            max_height = min(height[left], height[right]) * (right - left);
        }
        if(height[left] < height[right]){
            left++;
        } else {
            right--;
        }
    }

    return max_height;
}

int main(){
    vector<int> height = {1,8,6,2,5,4,8,3,7};
    cout << maxArea(height);
}