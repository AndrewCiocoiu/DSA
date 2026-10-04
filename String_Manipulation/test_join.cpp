#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main(){
    string data = "andrei,ana,maria,mara";
    stringstream ss(data);
    string tok;

    while(getline(ss, tok, ',')){
        cout << tok << "\n";
    }
}