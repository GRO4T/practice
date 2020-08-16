/*
    This solution is also O(N*log(N)) but fails at last performance test (0.596s > 0.352s)
*/


// you can use includes, for example:
#include <algorithm>
#include <map>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    std::map<int, int> occurMap;
    
    for (auto elem : A){
        auto it = occurMap.find(elem);
        if (it == occurMap.end()){
            occurMap.insert(std::pair<int, int>(elem, 1));
        }
        else{
            (it->second)++;
        }
    }
    
    /*
    for(auto it = occurMap.begin(); it != occurMap.end(); ++it){
        std::cout << it->first << " " << it->second << " " << "\n";
    }
    */
    
    for(auto it = occurMap.begin(); it != occurMap.end(); ++it){
        if (it->second % 2 == 1) return it->first;
    }
    return -1;
}