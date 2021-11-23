#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;

    while(t){
        int n;
        cin >> n;
        vector<int> first(n + 1,0);
        vector<int> second(n + 1,0);

        for(int i = 0; i < n;i++){
            int temp;
            cin >> temp;         
            first[i] = temp;               
        }

        for(int i = n - 1; i >= 0;i--){
            first[i] += first[i + 1];               
        }

        for(int i = 1; i < n + 1;i++){
            int temp;
            cin >> temp;
            second[i] = temp + second[i - 1];
        }

        int ans = INT32_MAX;
        for(int i = 0;i < n;i++){
            ans = min(ans,max(first[i + 1],second[i]));
        }
        cout << ans << '\n';
  
        t--;
    }
}