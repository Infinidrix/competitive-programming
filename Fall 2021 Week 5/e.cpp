#include <bits/stdc++.h>

using namespace std;

int main(){
    long long n;
    cin >> n;
    vector<long long> diffs(n);
    for (long long i = 0; i < n; i++){
        long long temp;
        cin >> temp;
        diffs[i] = temp;
    }
    for (long long i = 0; i < n; i++){
        long long temp;
        cin >> temp;
        diffs[i] -= temp;
        diffs[i] *= -1;
    }
    sort(diffs.begin(), diffs.end());
    long long ans = 0;
    for (long long i = 0; i < n; i++){
        long long curr = diffs[i];
        long long counts = upper_bound(diffs.begin(), diffs.end(), -curr - 1) - diffs.begin();
        ans += counts;
        if (curr < 0){
            ans--;
        }
    }
    cout << ans / 2 << endl;
}