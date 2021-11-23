#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    while (cin >> n){
        int prev;
        cin >> prev;
        vector<bool> visited(n, false);
        visited[0] = true;
        for (int i = 0; i < n - 1; i++){
            int temp;
            cin >> temp;
            int value = abs(temp - prev);
            if (value < n){
                visited[value] = true;
            }
            prev = temp;
        }
        bool found = (find(visited.begin(), visited.end(), false) != visited.end());
        if (!found){
            cout << "Jolly" << '\n';
        }
        else {
            cout << "Not jolly" << '\n';
        }
    }
}