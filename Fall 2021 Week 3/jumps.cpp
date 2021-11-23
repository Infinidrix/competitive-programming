#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;

    for (int i = 0; i < t; i++){
        int n;
        cin >> n;
        vector<int> arr(n + 1);
        for (int i = 1; i < arr.size(); i++){
            int temp;
            cin >> temp;
            arr[i] = temp;
        }
        int maxi = 0;
        for (int i = arr.size() - 1; i > 0; i--){
            if (i + arr[i] < (int) arr.size()){
                arr[i] += arr[arr[i] + i];
            }
            maxi = max(maxi, arr[i]);
        }
        cout << maxi << '\n';
    }
    cout << endl;
}