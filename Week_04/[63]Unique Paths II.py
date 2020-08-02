# A robot is located at the top-left corner of a m x n grid (marked 'Start' in t
# he diagram below). 
# 
#  The robot can only move either down or right at any point in time. The robot 
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in the d
# iagram below). 
# 
#  Now consider if some obstacles are added to the grids. How many unique paths 
# would there be? 
# 
#  
# 
#  An obstacle and empty space is marked as 1 and 0 respectively in the grid. 
# 
#  Note: m and n will be at most 100. 
# 
#  Example 1: 
# 
#  
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#  
#  Related Topics 数组 动态规划 
#  👍 387 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [0 for _ in range(m)]
        dp[0] = 1 - obstacleGrid[0][0]
        for col in range(1, m):
            dp[col] = dp[col - 1] * (1 - obstacleGrid[0][col])
        for row in range(1, n):
            dp[0] *= 1 - obstacleGrid[row][0]
            for col in range(1, m):
                dp[col] += dp[col - 1] if not obstacleGrid[row][col] else -dp[col]
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
