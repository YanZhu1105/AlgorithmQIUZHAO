# Given a triangle, find the minimum path sum from top to bottom. Each step you 
# may move to adjacent numbers on the row below. 
# 
#  For example, given the following triangle 
# 
#  
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#  
# 
#  The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11). 
# 
#  Note: 
# 
#  Bonus point if you are able to do this using only O(n) extra space, where n i
# s the total number of rows in the triangle. 
#  Related Topics 数组 动态规划 
#  👍 555 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle: return
        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]
# leetcode submit region end(Prohibit modification and deletion)
