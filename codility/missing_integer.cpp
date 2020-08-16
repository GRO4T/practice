// you can use includes, for example:

#include <algorithm>


// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    int smallest = 1;
    sort(A.begin(), A.end());
    
    for (auto integer : A){
        if (integer == smallest) smallest++;
    }
    
    return smallest;
}