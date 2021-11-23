#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    freopen("max-pair.in", "r", stdin);
    cin >> t;

    for (int i = 0; i < t; t++){
        vector<bool> visited(26, false);
        string input;
        cin >> input;
        int s = input.size();
        cout << (int)(input[0] - 'a') << endl;
        visited[(int)(input[0] - 'a')] = true;
        
        for (int j = 0; j < s; j++){
            if (!visited[(int)(input[j] - 'a')]){
                cout << max(j, s - j - 1) << endl;
                break;
            }
            if (!visited[(int)(input[s - j] - 'a')]){
                cout << max((s - j), s - (s - j) - 1) << endl;
                break;
            }
        }
    }
}