#include <bits/stdc++.h>

using namespace std;

int main(){
    int c;
    cin >> c;
    int prev = INT32_MAX, longest = 0, curr_len = 0;
    for (int i = 0; i < c; i++){
        int temp;
        cin >> temp;
        if (prev >= temp){
            curr_len = 1;
        } else {
            curr_len++;
        }
        prev = temp;
        longest = max(longest, curr_len);
    }
    cout << longest << endl;
}