#include <bits/stdc++.h>

using namespace std;

int main(){
    vector<pair<int, int>> dirs = {
        make_pair(-1, 0),
        make_pair(0, -1),
        make_pair(1, 0),
        make_pair(0, 1)
    };
    int s, p;
    while (true){
        cin >> s >> p;
        if (s == 0 && p == 0)
            break;
        int start_node = sqrt(p);
        if (start_node % 2 == 0)
            start_node--;
        int max_moves = 1, moves = 1, ind = 0;
        pair<int, int> loc = { (s / 2), (s / 2)};
        if (start_node > 1) {
            p++;
            p -= start_node * start_node;
            int push = (start_node - 1) >> 1;
            max_moves = start_node;
            loc = { (s / 2) - push, (s / 2) + push};
        }
        

        for (int i = 1; i < p; i++){
            loc = make_pair(loc.first + dirs[ind].first, loc.second + dirs[ind].second);
            moves--; 
            if (moves == 0){
                ind++;
                ind %= 4;
                if (ind % 2 == 0) {
                    max_moves++;
                }
                moves = max_moves;
            }
        }
        cout << "Line = " << s - loc.first << ", column = " << loc.second + 1<< ".\n";
    }
}