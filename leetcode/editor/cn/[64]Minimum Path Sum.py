# Given a m x n grid filled with non-negative numbers, find a path from top left
#  to bottom right which minimizes the sum of all numbers along its path. 
# 
#  Note: You can only move either down or right at any point in time. 
# 
#  Example: 
# 
#  
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
#  
#  Related Topics 数组 动态规划 
#  👍 608 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        dp = [row[:] for row in grid]
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            dp[i][0] += dp[i-1][0]
        for j in range(1, n):
            dp[0][j] += dp[0][j-1]
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] += min(dp[row-1][col], dp[row][col-1])
        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
S = Solution()
S.minPathSum([[1,3,1],[1,5,1],[4,2,1]])