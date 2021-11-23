#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        string input;
        cin >> input;
        int curr = 0, longest = 0;
        for (int j = 0; j < input.size(); j++){
            char in = input[j];
            if (in == 'L'){
                curr++;
            } else {
                curr = 0;
            }
            longest = max(longest, curr);
        }
        cout << longest + 1 << '\n';
    }
}