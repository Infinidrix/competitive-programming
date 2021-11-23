#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;

    cin >> t;
    for (int i = 0; i < t; i++){
        int temp_max = 0, ans = 0, sum = 0, n, m;
        cin >> n;
        for (int j = 0; j < n; j++){
            int temp;
            cin >> temp;
            sum += temp;
            temp_max = max(sum, temp_max);
        }
        ans += temp_max;
        temp_max = 0, sum = 0;
        cin >> m;
        for (int j = 0; j < m; j++){
            int temp;
            cin >> temp;
            sum += temp;
            temp_max = max(sum, temp_max);
        }
        cout << ans + temp_max << endl;
    }

}