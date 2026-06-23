#include <iostream>
#include <vector>
#include <print>

using namespace std;

int hamming_weight(int n){
    int count = 0;
    while(n){
        n = n & (n - 1);
        count++;
    }
    return count;
}

vector<int> countBits(int n) {
    vector<int> results;
    for(int i = 0; i <= n; i++){
        results.push_back(hamming_weight(i));
    }
    return results;
}

int main(){
    int n = 2;
    countBits(n);
    print("{}\n", countBits(n));
}