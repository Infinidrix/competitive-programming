#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, k;
    cin >> n >> k;

    vector<int> walks(n);
    for (int i = 0; i < n; i++){
        int temp;
        cin >> temp;
        walks[i] = temp; 
    }
    // cout << "walks" << '\n';
    // for (int i = 0; i < n - 1; i++){
    //     cout << walks[i] << ' ';
    // }
    // cout << walks[n - 1] << endl;
    int adds = 0;
    for (int i = 1; i < n; i++){
        int diff = max(0, k - (walks[i] + walks[i - 1]));
        adds += diff;
        walks[i] += diff;
    }
    cout << adds << '\n';
    for (int i = 0; i < n - 1; i++){
        cout << walks[i] << ' ';
    }
    cout << walks[n - 1] << endl;
}