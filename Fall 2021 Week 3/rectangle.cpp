#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, m;
    cin >> n >> m;

    vector<vector<int>> mat(n, vector<int>(m));
    unsigned long long res = 0;
    int bc = 0, wc = 0;
    for (int i = 0; i < n; i++){
        bc = 0;
        wc = 0;
        for (int j = 0; j < m; j++){
            int temp;
            cin >> temp;
            mat[i][j] = temp;
            if (temp == 0){
                wc++;
            } else {
                bc++;
            }
        }
        res += (1ULL << wc) + (1ULL << bc) - 2;
    }
    for (int j = 0; j < m; j++){
        wc = bc = 0;
        for (int i = 0; i < n; i++){
            if (mat[i][j] == 0){
                wc++;
            } else{
                bc++;
            }
        }
        res += (1ULL << wc) + (1ULL << bc) - 2;
    }
    cout << res - (n * m) << endl; 
}