#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;

    for (int i = 0; i < t; i++){
        int n, result = 0;
        cin >> n;
        string input;
        cin >> input;
        result = int(input[n - 1] - '0');
        for (int i = 0; i < n - 1; i++){
            if (input[i] != '0'){
                result += 1 + (int) (input[i] - '0');
            }
        }
        cout << result << '\n';
    }
    cout << endl;
}