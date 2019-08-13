#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Solution {
   public:
    vector<int> sortArrayByParityII(vector<int>& A) {
        vector<int> even, odd;
        for (int i : A) {
            if (i % 2 == 0) {
                even.push_back(i);
            } else {
                odd.push_back(i);
            }
        }
        vector<int>::iterator even_it = even.begin();
        vector<int>::iterator odd_it = odd.begin();
        vector<int> result;

        int N = A.size();
        for (int i = 0; i < N; ++i) {
            if (i % 2 == 0) {
                result.push_back(*even_it);
                ++even_it;
            } else {
                result.push_back(*odd_it);
                ++odd_it;
            }
        }
    }
};

int main(void) {
    Solution sol;
    vector<int> nums = {4, 2, 5, 7};
    sol.sortArrayByParityII(nums);
    return 0;
}