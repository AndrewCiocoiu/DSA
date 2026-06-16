#include <iostream>

using namespace std;

bool isPalindrome(int x) {
        if(x < 0){
            return false;
        }
        else if(x < 10){
            return true;
        }

        int aux = x;
        long long new_num = 0;
        while(aux > 0){
            new_num = new_num * 10 + aux % 10;
            aux /= 10;
        }
        
        if(new_num == x){
            return true;
        } else {
            return false;
        }
    }

int main(){
    return 0;
}