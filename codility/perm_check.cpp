// you can use includes, for example:
#include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    int n = A.size();
    sort(A.begin(), A.end());
    
    if (A[0] != 1 || A[n - 1] != n) 
        return 0;
    
    for (int i = 1; i < n; ++i){
        if (A[i] != A[i - 1] + 1) return 0;
    }
    
    return 1;
    
}