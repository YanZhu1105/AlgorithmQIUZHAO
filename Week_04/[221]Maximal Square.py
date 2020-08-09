# Given a 2D binary matrix filled with 0's and 1's, find the largest square cont
# aining only 1's and return its area. 
# 
#  Example: 
# 
#  
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
#  Related Topics 动态规划 
#  👍 496 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        dp = [list(map(int, row)) for row in matrix]
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                dp[row][col] = (min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1 if matrix[row][col] == '1' else 0)
        return max(map(max, dp)) ** 2

# leetcode submit region end(Prohibit modification and deletion)
S = Solution()
S.maximalSquare([["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]])