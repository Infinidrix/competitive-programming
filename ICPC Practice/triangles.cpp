#include <bits/stdc++.h>

using namespace std;

int main(){
    long long n;
    cin >> n;
    while (n >= 3){
        unsigned long long answer = 0;
        for (long long i = 4; i <= n; i++){
            answer += ((i - 2) / 2) * (n - i + 1ull);
        }
        cout << answer << '\n';
        cin >> n;
    }

}