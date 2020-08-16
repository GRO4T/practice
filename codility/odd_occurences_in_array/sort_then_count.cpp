/*
    This solution is O(N*log(N)) and passes all tests
*/


// you can use includes, for example:
#include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    if (A.size() == 1) return A[0];

    int currVal;
    int counter = 0;
    
    std::sort(A.begin(), A.end());
    currVal = A[0];
    
    /*
    for (auto elem : A){
        std::cout << elem << " ";
    }
    std::cout << std::endl;
    */
    
    for (auto elem : A){
        if (elem == currVal) counter++;
        else{
            if (counter % 2 == 1) return currVal;
            currVal = elem;
            counter = 1;
        }
    }
    return currVal;
}