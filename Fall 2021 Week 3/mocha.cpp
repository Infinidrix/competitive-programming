#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;

    for (int i = 0; i < t; i++){
        queue<int> q;
        int n;
        string choices = "RB";
        cin >> n;
        string input;
        cin >> input;
        for (int j = 0; j < n; j++){
            if (input[j] != '?'){
                q.push(j);
            }
        }
        if (q.empty()){
            input[0] = 'B';
            q.push(0);
        }
        while (!q.empty()){
            int ind = q.front();
            q.pop();

            for (int next = -1; next < 2; next++){
                if (ind + next >= 0 && ind + next < n && input[ind + next] == '?'){
                    if (input[ind] == 'R'){
                        input[ind + next] = 'B';
                    } else{
                        input[ind + next] = 'R';
                    }
                    q.push(ind + next);
                }
            }
        }
        cout << input << '\n';
    }
    cout << endl;
}