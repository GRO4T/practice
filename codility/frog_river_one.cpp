// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(int X, vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    int canPassUpTo = 0;
    std::vector<bool> leaves(X + 1, false);
    
    for (unsigned i = 0; i < A.size(); ++i){
        leaves[A[i]] = true;
        while (leaves[canPassUpTo + 1] == true) canPassUpTo++;
        
        if (canPassUpTo == X) return i;
    }
    
    return -1;
}