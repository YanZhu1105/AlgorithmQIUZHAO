# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle c
# ontaining only 1's and return its area. 
# 
#  Example: 
# 
#  
# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6
#  
#  Related Topics 栈 数组 哈希表 动态规划 
#  👍 588 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        dp = [0] * len(matrix[0])
        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            max_area = max(max_area, self.leetcode84(dp))
        return max_area

    def leetcode84(self, heights):
        heights = [0] + heights + [0]
        stack = [0, ]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                curr_h = heights[stack.pop()]
                area = curr_h * (i - 1 - stack[-1])
                res = max(area, res)
            stack.append(i)
        return res
# leetcode submit region end(Prohibit modification and deletion)
S = Solution()
S.maximalRectangle([2,1,5,6,2,3])
