#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;

    for (int i = 0; i < t; i++){
        long long n, wire, curr = 1, count = 0;
        cin >> n >> wire;
        n--;

        while (n > 0 && curr <= wire){
            n -= curr;
            count++;
            curr <<= 1;
        }
        if (n <= 0){
            cout << count << '\n';
        } else {
            cout << count + (long long ) ceill( (n * 1.0L) / wire) << '\n';
        }
    }
    cout << endl;
}