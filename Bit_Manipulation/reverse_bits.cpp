#include <iostream>

using namespace std;

uint32_t reverseBits(uint32_t n) {
    int new_num = 0;
    for(int i = 0; i < 32; i++){
        int last_bit = n & 1;
        new_num = (new_num << 1) | last_bit;
        n = n >> 1;
    }
    return new_num;
}

int main(){
    int n = 43261596;
    reverseBits(n);
    cout << reverseBits(n);
}