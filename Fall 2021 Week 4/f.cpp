#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    
    for (int i = 0; i < t; i++){
        int n;
        cin >> n;
        // cout << "This is n " << n;
        vector<vector<int>> graph(n + 1);
        vector<int> incoming(n + 1, 0);
        for (int j = 1; j < n + 1; j++){
            int k;
            cin >> k;
            incoming[j] = k;
            for (; k > 0; k--){
                int temp;
                cin >> temp;
                graph[temp].push_back(j);
            }
        }
        priority_queue<int, vector<int>, greater<int>> first, second;
        // cout << "Incoming ";
        // for (int k = 0; k < n + 1; k++){
        //     cout << incoming[k] << " " << k  << " " << endl;
        // }
        for (int j = 1; j < n + 1; j++){
            if (incoming[j] == 0){
                first.push(j);
            }
        }
        int ans = 1, count = 0;
        while (!first.empty() || !second.empty()){
            if (first.empty()){
                auto temp = first;
                first = second;
                second = temp;
                ans++;
            }
            int curr = first.top();
            first.pop();
            count++;
            // cout << "popped " << curr << endl;
            for (auto& neigh: graph[curr]){
                
                // cout << "at " << neigh << " with incoming " << incoming[neigh] << endl;
                incoming[neigh]--;
                if (incoming[neigh] == 0){
                    if (curr > neigh){
                        second.push(neigh);
                    } else {
                        first.push(neigh);
                    }
                }
            }
        }
        cout << ((count == n) ? ans : -1) << '\n';
    }
}