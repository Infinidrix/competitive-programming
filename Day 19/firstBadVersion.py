# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
 
 
# https://leetcode.com/problems/first-bad-version/

class Solution:
    def bad_finder(self, lower, upper):
        if lower < upper:
            mid = (lower + upper)//2
            if isBadVersion(mid):
                return self.bad_finder(lower, mid)
            else:
                return self.bad_finder(mid + 1, upper)
        return lower
            
    
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.bad_finder(0, n)