#include <bits/stdc++.h>

using namespace std;

// int solve(int n,vector<int> arr){
//     vector<int> minR(n,)
// }


int main(){
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        int n;
        cin >> n;
        vector<int> list(n, 0);
        for (int j = 0; j < n; j++){
            int temp;
            cin >> temp;
            list[j] = temp;
        }
        int count = n;
        bool gotIt = false;
        for (int left = 0, right = n - 1; left < right; ){
            if (list[left] == count){
                count--;
                left++;
            } else if (list[right] == count){
                count--;
                right--;
            } else {
                cout << "YES" << '\n';
                cout << left + 1  << " " << (int) (find(list.begin(), list.end(), count)  - list.begin()) + 1<< " " << right + 1 << '\n';
                gotIt = true;
                break;
            }
        }
        if (!gotIt){
            cout << "NO" << '\n';
        }
    }
    cout << endl;
}