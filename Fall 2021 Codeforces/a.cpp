#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;

    for (int i = 0; i < t; i++){
        int a, b, c;
        cin >> a >> b >> c;
        int mid = a + b + c - min(a, min(b, c)) - max(a, max(b, c));
        int rest = a + b + c - mid;
        int ans = (mid - 2 * rest) % 3;
        cout << ((ans == 0) ? 0 : 1) << '\n';
    }

}