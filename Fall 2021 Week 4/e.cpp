#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        int n, x;
        cin >> n >> x;

        vector<int> nums;
        for(int j = 0; j < n; j++){
            int temp;
            cin >> temp;
            nums.push_back(temp);
        }
        sort(nums.begin(), nums.end());
        int count = 0, ans = 0;
        for (int j = n - 1; j >= 0; j--){
            count++;
            if (count * nums[j] >= x){
                ans++;
                count = 0;
            }
        }
        cout << ans << '\n';
    }
}