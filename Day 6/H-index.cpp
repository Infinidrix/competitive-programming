#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int hIndex(vector<int>& citations) {
        int size = citations.size();
        if (size==0) return 0;
        sort(citations.begin(), citations.end());
        int i;
        for (i = 1; i <= size; i++){
            if(citations[size-i]<i){
                i--;
                return i;
            }
        }
        return i-1;
    }
};