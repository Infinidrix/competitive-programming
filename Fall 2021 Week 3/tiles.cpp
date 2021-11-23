#include <bits/stdc++.h>

using namespace std;


long long powerMod(long long a, long long b, int m)
{
    long long res = 1;
    a = a % m;
    for(int i=1 ; i<=b ; ++i)
        res = (res * a) % m;
    
    return res;
}

int main(){
    long long n, m;

    cin >> n >> m;

    cout << (powerMod(2, n, 998244353) * powerMod(2, m, 998244353 )) % 998244353 << endl;
}