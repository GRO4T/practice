// you can use includes, for example:
#include <algorithm>
#include <cmath>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    int sum = 0;
    for (auto elem : A){
        sum += elem;
    }
    
    int sumLeft = A[0], sumRight = sum - A[0];
    unsigned diff = std::abs(sumLeft - sumRight);
    unsigned bestDiff = diff;

    for (unsigned p = 2; p < A.size(); ++p){
        sumLeft += A[p - 1];
        sumRight -= A[p - 1];
        diff = std::abs(sumLeft - sumRight);
        
        if (diff < bestDiff){
            bestDiff = diff;
        }
    }
    
    return bestDiff;
}