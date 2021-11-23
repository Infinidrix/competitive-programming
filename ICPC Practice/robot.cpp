#include <bits/stdc++.h>

using namespace std;

int main(){
    int t; 
    cin >> t;
    for (int i = 0; i < t; i++){
        int pos = 0, inst;
        cin >> inst;
        vector<int> insts(inst);
        for (int j = 0; j < inst; j++){
            string in;
            cin >> in;
            if (in == "LEFT"){
                pos--;
                insts[j] = -1;
            } else if (in == "RIGHT"){
                pos++;
                insts[j] = 1;
            } else {
                cin >> in;
                int loc;
                cin >> loc;
                pos += insts[loc - 1];
                insts[j] = insts[loc - 1];
            }
        }
        cout << pos << '\n';
    }
}