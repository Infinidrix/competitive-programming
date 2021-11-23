#include <bits/stdc++.h>

using namespace std;

unsigned int gcd (unsigned int n1, unsigned int n2) {
    return (n2 == 0) ? n1 : gcd (n2, n1 % n2);
}

int main(){
    int y, w;
    cin >> y >> w;
    if (y < w){
        y = w;
    }
    w = (6 - y + 1);

    cout << w / gcd(w, 6) << "/" << 6 / gcd(w, 6) << endl;
}