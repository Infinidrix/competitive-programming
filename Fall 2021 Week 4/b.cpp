#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;

    for (int i = 0; i < t; i++){
        int n;
        cin >> n;
        cout << 2 << '\n';
        int prev = n;
        for (int j = n - 1; j > 0; j--){
            cout << prev << " " << j << '\n';
            prev = (prev + j) / 2 + (prev + j) % 2;
        }
    }
    cout << endl;
}