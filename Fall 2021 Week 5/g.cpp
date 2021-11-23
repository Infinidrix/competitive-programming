#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, h, l, r;
    cin >> n >> h >> l >> r;
    vector<int> hours;
    for (int i = 0; i < n; i++){
        int temp;
        cin >> temp;
        hours.push_back(temp);
    }

    // vector<vector<int>> dp(n + 1, vector(0, h));
    int dp[n+1][h];
    for (int i = 0; i < h; i++){
        dp[n][i] = 0;
    }
    for (int i = n - 1; i >= 0; i--){
        for(int j = 0; j < h; j++){
            int new_time = (j + hours[i]) % h;
            int add = (new_time >= l && new_time <= r) ? 1 : 0;
            int new_time_minus = (j + hours[i] - 1) % h;
            int add_minus = (new_time_minus >= l && new_time_minus <= r) ? 1 : 0; 
            dp[i][j] = max(dp[i + 1][new_time] + add, dp[i+1][new_time_minus] + add_minus);
        }
    }
    cout << dp[0][0] << endl;
}