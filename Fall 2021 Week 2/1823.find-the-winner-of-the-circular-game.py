#
# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
#

# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        count = k
        out_count = curr = 0
        out = [False for i in range(n)]
        while out_count < n - 1:
            if not out[curr]:
                count -= 1
            if count == 0:
                out[curr] = True
                out_count += 1
                count = k
            curr = (curr + 1) % n
        res = [i + 1 for i in range(len(out)) if not out[i]]
        return res[0]
        # @lc code=end

