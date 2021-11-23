#include <bits/stdc++.h>

using namespace std;

int main(){
    long long n, m;

    cin >> n >> m;

    vector<long long> prefix(n+1, 0);
    for (int i = 1; i <= n; i++){
        long long temp;
        cin >> temp;
        prefix[i] = prefix[i-1] + temp;
    }

    int prefix_ind = 1;
    for (int i = 0; i < m; i++) {
        long long query;
        cin >> query;
        while (prefix[prefix_ind] < query){
            prefix_ind++;
        }
        cout << prefix_ind << " " << query - prefix[prefix_ind - 1] << '\n';
    }
}