#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, x;
    freopen("binary.in", "r", stdin);
    cin >> n >> x;
    string input;
    cin >> input;

    for (int k = 1; k < n; k++){
        int ones = 0, zeros = 0;
        for (int i = 0; i < n - k; i++){
            if (input[i] == '0'){
                zeros++;
            } else {
                ones++;
            }
            if (i + k >= n - k && i + k < n){
                if (input[i + k] == '0'){
                    zeros++;
                } else {
                    ones++;
                }
            }
        }
        cout << zeros << " " << ones << endl;
        if (min(ones, zeros) <= x){
            cout << k << endl;
            break;
        }
    }
}