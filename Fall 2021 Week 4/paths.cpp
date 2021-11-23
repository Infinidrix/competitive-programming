#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int countRestrictedPaths(int n, vector<vector<int>>& edges) {
        vector<int> paths(n, 0);
        vector<vector<pair<int, int>>> graph(n + 1);
        priority_queue<pair<int, int>> q(vector<pair<int, int>>, [](pair<int, int>& a, pair<int, int>& b) {
            return a.first < b.first;
        });
        for (auto& edge: edges){
            graph[edge[0]].push_back(make_pair(edge[1], edge[2]));
            graph[edge[1]].push_back(make_pair(edge[0], edge[2]));
        }
        paths[n] = 1;
        q.push(make_pair(n, 1));
        while (!q.empty()){
            
        }
    }
};