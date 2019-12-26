#include <algorithm>
#include <vector>
#include <string>

// https://leetcode.com/problems/valid-anagram/

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()){
            return false;
        }
        vector<char> s_char;
        vector<char> t_char;
        for(int i = 0; i < s.size(); i++){
            s_char.push_back(s.at(i));
            t_char.push_back(t.at(i));
        }
        sort(s_char.begin(), s_char.end());
        sort(t_char.begin(), t_char.end());
        if (s_char == t_char){
            return true;
        }
        return false;
    }
};
