# A robot is located at the top-left corner of a m x n grid (marked 'Start' in t
# he diagram below). 
# 
#  The robot can only move either down or right at any point in time. The robot 
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in the d
# iagram below). 
# 
#  How many possible unique paths are there? 
# 
#  
# Above is a 7 x 3 grid. How many possible unique paths are there? 
# 
#  
#  Example 1: 
# 
#  
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-righ
# t corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
#  
# 
#  Example 2: 
# 
#  
# Input: m = 7, n = 3
# Output: 28
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= m, n <= 100 
#  It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9. 
#  
#  Related Topics 数组 动态规划 
#  👍 626 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1 for _ in range(m)]

        for row in range(1, n):
            for col in range(1, m):
                dp[col] += dp[col - 1]

        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
