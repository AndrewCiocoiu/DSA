#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int lastStoneWeight(vector<int>& stones) {
    priority_queue<int> maxHeap(stones.begin(), stones.end());
    while (maxHeap.size() > 1){
        int stone_1 = maxHeap.top();
        maxHeap.pop();
        int stone_2 = maxHeap.top();
        maxHeap.pop();

        if(stone_1 == stone_2){
            continue;
        }
        maxHeap.push(stone_2 - stone_1);
    }
    if(!maxHeap.empty()){
        return maxHeap.top();
    } else {
        return  0;
    }
}

int main(){
    vector<int> stones = {2,7,4,1,8,1};
    cout << lastStoneWeight(stones);
}