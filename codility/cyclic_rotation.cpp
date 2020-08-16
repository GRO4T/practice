// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

vector<int> solution(vector<int> &A, int K) {
    // write your code in C++14 (g++ 6.2.0)
    unsigned size = A.size();
    vector<int> rotatedA(size, 0);

    for (unsigned i = 0; i < size; ++i){
        rotatedA[(i + K) % size] = A[i];
    }
    
    /*
    for (auto e : rotatedA){
        std::cout << e << " ";
    }
    std::cout << std::endl;
    */
    
    return rotatedA;
}