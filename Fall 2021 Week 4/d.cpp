#include <bits/stdc++.h>

using namespace std;

bool valid(vector<int> &count){
    bool isValid = true;
    for(int i = 1; i < 4;i++){
        if(count[i] < 1){
            return false;
        }
    }
    return true;
}

int main(){
    int t;
    cin >> t;

    while(t){
        string str;
        cin >> str;

        vector<int> count(4,0);
        int n = str.size();
        int ans = 0;
        int left = 0;

        for(int i = 0;i < n;i++){
            count[(int)(str[i] - '0')]++;
            while(valid(count)){
                ans = ans == 0 ? i - left + 1 : min(ans,i - left + 1);
                count[(int)(str[left] - '0')]--;
                left++;
            }
        }

        cout << ans << "\n";
        t--;
    }
}