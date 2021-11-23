#include <bits/stdc++.h>

using namespace std;

int main(){
    int t; 
    cin >> t;
    for (int i = 0; i < t; i++){
        int n, k;
        cin >> n >> k;
        int ans = 0;
        for (int j = 0; j <= n; j++){
            ans += ((k & 1) ^ ((k & 2) >> 1)) << j;
            k >>= 1;
        }

        cout << ans << '\n';
    }

}
