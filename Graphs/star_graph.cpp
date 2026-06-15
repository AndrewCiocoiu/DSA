#include <iostream>
#include <algorithm> 
#include <vector>


using namespace std;

int main() {
    vector<vector<int>> edges = {
        {1, 2},
        {2, 3},
        {4, 2}
    };

    if (ranges::contains(edges[1], edges[0][0])) {
        cout << "Center is: " << edges[0][0] << endl;
    } 
    else {
        cout << "Center is: " << edges[0][1] << endl;
    }

    return 0;
}