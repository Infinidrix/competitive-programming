#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;

    for (int i = 0; i < t; i++){
        int n, k;
        cin >> n >> k;
        vector<int> locs(k);
        for (int j = 0; j < k; j++){
            int temp;
            cin >> temp;
            locs[j] = temp - 1;
        }
        priority_queue<pair<long long, int>> q;
        vector<long long> visited(n, 0);
        for (int j = 0; j < k; j++){
            int temp;
            cin >> temp;
            q.push(make_pair(-temp, locs[j]));
        }

        while (!q.empty()){
            pair<long long, int> curr = q.top();
            q.pop();
            int loc = curr.second;
            long long temp = -curr.first;
            if (visited[loc] == 0){
                visited[loc] = temp;
            } else {
                continue;
            }
            if (loc > 0 && visited[loc - 1] == 0){
                // visited[loc - 1] = temp + 1;
                q.push(make_pair(-(temp + 1), loc - 1));
            } 
            if (loc < visited.size() - 1 && visited[loc + 1] == 0){
                // visited[loc + 1] = temp + 1;
                q.push(make_pair(-(temp + 1), loc + 1));
            }
        }
        for (int i = 0; i < visited.size() - 1; i++){
            cout << visited[i] << " ";
        }
        cout << visited[visited.size() - 1] << '\n';
    }
    cout << endl;
}