#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;

    while (t--){
        int n;
        cin >> n;
        int last_zero = -1, prev_one = -1;
        string input;
        cin >> input;
        for (int i = 0; i < input.size(); i++){
            if (input[i] == '0'){
                if (i > 0 && input[i - 1] == '1'){
                    prev_one = i - 1;
                }
                last_zero = i;
            }
        }
        if (prev_one == -1 || last_zero == -1){
            cout << 0 << '\n';
            continue;
        }
        cout << 1 << '\n';
        vector<int> answer;
        for (int i = 0; i < input.size(); i++){
            if (i <= last_zero){
                if (input[i] == '1'){
                    answer.push_back(i + 1);
                } else if (i >= prev_one){
                    answer.push_back(i + 1);
                }
            }
        }
        cout << answer.size() << " ";
        for (int i = 0; i < answer.size() - 1; i++){
            cout << answer[i] << " ";
        }
        if (answer.size() >= 1){
            cout << answer[answer.size() - 1];
        }
        cout << '\n';
    }
}