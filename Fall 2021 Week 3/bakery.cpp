#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int get_price(vector<int>& nums, int boxes, int ind, unordered_set<int>& visited, unordered_map<int, int>& dp){
    int state = ind << 7 | boxes;
    if (dp.find(state) != dp.end() && visited.size() == 0){
        return dp[state];
    }
    int l = visited.size();
    if (ind >= nums.size()){
        // for (auto& num: visited)
        //     cout << num << " ";
        // cout << endl;
        visited.clear();
        return l;
    }
    // cout << ind << " ind " << endl;
    visited.insert(nums[ind]);
    l = visited.size();
    int res = get_price(nums, boxes, ind + 1, visited, dp);
    if (boxes > 0){
        // cout << visited.size() << " and ind " << ind << endl;
        int res2 = get_price(nums, boxes - 1, ind + 1, visited, dp);
        // cout << visited.size() << " out ind " << ind << " result " << res2 << endl;
        dp[(ind + 1) << 7 | (boxes - 1)] = res2;
        return max(res, res2 + l);
    }
    return res;
}


int main(){
    int n, k;
    cin >> n >> k;
    vector<int> nums = vector<int>();
    for(int i = 0; i < n; i++){
        int num;
        cin >> num;
        nums.push_back(num);
    }
    vector<int> postfix(n, 0);
    unordered_set<int> visited;
    unordered_map<int, int> dp;
    for (int i = n - 1; i >= 0; i--){
        visited.insert(nums[i]);
        dp[i << 7 | 1] = visited.size();
    }
    dp[n << 7 | 1] = 0;
    int max_price = visited.size();
    for (int i = 2; i <= k; i++){
        visited.clear();
        for (int j = 1; j < n; j++){
            int curr_price = 0;
            visited.insert(nums[j]);
            dp[j << 7 | i] = visited.size() + dp[(j + 1) << 7 | i - 1];
            max_price = max(max_price, dp[j << 7 | i]);
        }
    }
    for (auto& [key, value]: dp){
        cout << "key ind: " << (key >> 7) << " key boxes: " << (key & 0x7f) << " value: " << value << endl;
    }

    cout << max_price << endl; 
}