#include <bits/stdc++.h>

using namespace std;

int main(){
    int t; 
    cin >> t;
    for (int i = 0; i < t; i++){
        int maxRel = INT32_MIN;
        vector<pair<string, int>> websites;
        for (int j = 0; j < 10; j++){
            string website;
            int relevenace;
            cin >> website >> relevenace;
            maxRel = max(maxRel, relevenace);
            websites.push_back(make_pair(website, relevenace));
        }
        cout << "Case #" << i + 1 << ":\n";
        for (int j = 0; j < 10; j++){
            if (websites[j].second == maxRel){
                cout << websites[j].first << '\n';
            }
        }
    }
}
