#include <bits/stdc++.h>

using namespace std;

int main(){
    unordered_map<int, int> counts;
    int t;
    cin >> t;

    for (int i = 0; i < t; i++){
        int n, k;
        cin >> n >> k;
        counts.clear();
        for (int j = 0; j < n; j++){
            int temp;
            cin >> temp;
            temp = (k - (temp % k)) % k;
            if (counts.find(temp) == counts.end()){
                counts[temp] = 0;
            }
            counts[temp]++;
        }
        int maxi = 0, max_val = 0;
        for (auto& entry: counts){
            int key = entry.first;
            int val = entry.second;
            // cout << "Key " << key << " val " << val << endl;
            if (key == 0)
                continue;
            if (maxi < val - 1){
                max_val = key + 1;
                maxi = val - 1;
            } else if (maxi == val - 1){
                max_val = max(max_val, key + 1);
            }
        }
        // cout << "Max iters " << maxi << " max val " << max_val << endl;
        cout << (((k) * 1ll) * (maxi)) + max_val << '\n'; 
    }
    cout << endl;
}