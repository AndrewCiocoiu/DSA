#include <iostream>
#include <vector>
#include <queue>
#include <cmath>


using namespace std;


struct CustomCompare{
    double calculate_distance_from_origin(const vector<int>& point){
        return sqrt(point[0] * point[0] + point[1] * point[1]);
    }

    bool operator()(const vector<int>& el_a, const vector<int>& el_b){
        return calculate_distance_from_origin(el_a) > calculate_distance_from_origin(el_b);
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<vector<int>, vector<vector<int>>, CustomCompare> minHeap;

        vector<vector<int>> results;

        for(auto & point : points){
            minHeap.push(point);
        }

        for(int i = 0; i < k; i++){
            results.push_back(minHeap.top());
            minHeap.pop();
        }

        return results;


}

int main(){
    vector<vector<int>> points = {{0,2},{2,2}};
    int k = 1;
}