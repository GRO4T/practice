// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(int N) {
    // write your code in C++14 (g++ 6.2.0)
    unsigned binaryGap = 0;
    unsigned currentBinaryGap = 0;
    bool firstOne = false;
    
    //std::cout << "N = " << N << std::endl;
    
    // convert to binary array
    for (int i = 0; i < 32; ++i){
        int x = (N >> i) & 1;
        
        //std::cout << x;
        
        if (!firstOne && x == 1) firstOne = true;
        else if (firstOne){
            if (x == 0) currentBinaryGap++;
            else if (x == 1){
                if (currentBinaryGap > binaryGap)
                    binaryGap = currentBinaryGap;
                currentBinaryGap = 0;
            }
        }
    }
    //std::cout << std::endl;
    
    
    return binaryGap;
}
