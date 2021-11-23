#include <bits/stdc++.h>

using namespace std;

int main(){
    int a, b;
    long long res = INT32_MAX;
    cin >> a >> b;
    if (a > b){
        int temp = a;
        a = b;
        b = temp;
    }
    for (int i = a; i <= b; i++){
        long long temp = ((i - a) * (i - a + 1)) / 2;
        temp += ((b - i) * (b - i + 1)) / 2;
        if (temp <= res){
            res = temp;
        } else{
            cout << res << endl;
            return 0;
        }
    }
    cout << res << endl;
    return 0;
}