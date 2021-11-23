#include <bits/stdc++.h>

using namespace std;

int main(){
    long long big_const = 1ll << 32;
    int t;
    cin >> t;

    for (int i = 0; i < t; i++){
        int n;
        cin >> n;
        vector<vector<int>> graph(n);
        vector<pair<int, int>> nodes(n);
        vector<int> incoming(n);
        vector<bool> visited(n, false);
        unordered_map<long long, long long> dp;
        queue<int> q;

        for (int j = 0; j < n; j++){
            int l, r;
            cin >> l >> r;
            nodes[j] = make_pair(l, r);
        }

        for (int j = 0; j < n - 1; j++){
            int u, v;
            cin >> u >> v;
            graph[u - 1].push_back(v - 1);
            graph[v - 1].push_back(u - 1);
            incoming[u - 1]++;
            incoming[v - 1]++;
        }
        for (int j = 0; j < n; j++){
            if (incoming[j] == 1){
                q.push(j);
            }
        }
        long long max_possible = 0;
        while (!q.empty()){
            int curr = q.front();
            q.pop();
            auto curr_node = nodes[curr];
            if (visited[curr]){
                continue;
            }
            visited[curr] = true;
            incoming[curr]--;
            long long min_ans = 0, max_ans = 0;
            for (auto& neighbours: graph[curr]){
                if (incoming[neighbours] > 1){
                    incoming[neighbours]--;
                    if (incoming[neighbours] == 1){
                        q.push(neighbours);
                    }
                } else if (incoming[neighbours] == 0){
                    min_ans += max(abs(curr_node.first - nodes[neighbours].first) + dp[big_const | neighbours], abs(curr_node.first - nodes[neighbours].second) + dp[neighbours]);
                    max_ans += max(abs(curr_node.second - nodes[neighbours].first) + dp[big_const | neighbours], abs(curr_node.second - nodes[neighbours].second) + dp[neighbours]);
                }
            }
            dp[big_const | curr] = min_ans;
            dp[curr] = max_ans;
            max_possible = max(max_possible, max(min_ans, max_ans));
        }
        cout << max_possible << endl;
    }
    cout << endl;
}