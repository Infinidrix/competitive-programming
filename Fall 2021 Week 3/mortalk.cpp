#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;

    for (int i = 0; i < t; i++){
        int n, k;
        cin >> n;
        vector<int> bosses(n + 5, 0);
        vector<int> dp(n + 5, 0);
        for (int j = 0; j < n; j++){
            int temp;
            cin >> temp;
            bosses[j] = temp;
            dp[j] = temp;
        }
        for (int j = n - 1; j >= 0; j--){
            int fp = bosses[j];
            int add = min(dp[j + 2], dp[j + 3]);
            add = min(add, dp[j + 3] + bosses[j + 1]);
            add = min(add, dp[j + 4] + bosses[j + 1]);
            dp[j] = fp + add;
        }
        cout << dp[0] << '\n';
    }
    cout << endl;
}