#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    freopen("two2.in", "r", stdin);
    cin >> t;
    for (int i = 0; i < t; i++){
        int num;
        cin >> num;
        if (num % 2 == 1){
            cout << -1 << '\n';
        } else {
            cout << num / 2 << '\n';
        }
    }
    cout << endl;
}