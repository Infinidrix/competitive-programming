#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;

    cin >> n;
    vector<vector<int>> graph(n + 1);
    queue<pair<int, int>> q;
    for (int i = 0; i < n; i++){
        int temp; 
        cin >> temp;
        if (temp != -1){
            graph[temp].push_back(i+1);
        } else{
            // node, depth
            q.push(make_pair(i+1, 1));
        }
    }
    int ans = 0;
    while (!q.empty()){
        auto curr = q.front();
        q.pop();
        ans = max(ans, curr.second);
        for (auto& neighbour: graph[curr.first]){
            q.push(make_pair(neighbour, curr.second + 1));
        }
    }
    cout << ans << endl;
}

