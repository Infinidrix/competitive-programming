
# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    
    def longest_palindrome(self, string, start, end, checked):
        if start == end:
            return 1
        if start > end:
            return 0
        if (start, end) in checked:
            return checked[(start, end)]
        if string[start] == string[end]:
            checked[(start, end)] = 2 + self.longest_palindrome(string, start + 1, end - 1, checked)
            return checked[(start, end)]
        checked[(start, end)] = max(self.longest_palindrome(string, start + 1, end, checked), self.longest_palindrome(string, start, end - 1, checked))
        return checked[(start, end)]
    
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longest_palindrome(s, 0, len(s)-1, {}) if len(s) > 0 else 0
