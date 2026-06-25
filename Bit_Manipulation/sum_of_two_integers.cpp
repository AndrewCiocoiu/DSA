#include <iostream>

using namespace std;

int getSum(int a, int b) {
    int c_in = 0;
    int sum = 0;
    for(int i = 0; i < 32; i++){
        int a_bit = a & 1;
        int b_bit = b & 1;

        int current_sum_bit = a_bit ^ b_bit ^ c_in;

        sum = sum | (current_sum_bit << i);
        c_in = (a_bit & b_bit) | (a_bit & c_in) | (b_bit & c_in);
        a = a >> 1;
        b = b >> 1;
    }
    return sum;
}

int main(){
    int a = 5;
    int b = 2;
    cout << getSum(a, b);    
}