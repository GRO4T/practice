// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

vector<int> solution(int N, vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    int maxCounter = 0;
    int lastUpdate = 0;
    std::vector<int> counters(N, 0);
    
    for (auto operation : A){
        if (operation <= N){
            if (counters[operation - 1] < lastUpdate)
                counters[operation - 1] = lastUpdate + 1;
            else
                counters[operation - 1]++;
            
            
            if (counters[operation - 1] > maxCounter){
                maxCounter = counters[operation - 1];
            }
        }
        else{
            lastUpdate = maxCounter;
        }
    }
    
    for (int i = 0; i < counters.size(); ++i){
        if (counters[i] < lastUpdate)
            counters[i] = lastUpdate;
    }
    
    return counters;
}
