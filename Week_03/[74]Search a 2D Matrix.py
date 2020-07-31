# Write an efficient algorithm that searches for a value in an m x n matrix. Thi
# s matrix has the following properties: 
# 
#  
#  Integers in each row are sorted from left to right. 
#  The first integer of each row is greater than the last integer of the previou
# s row. 
#  
# 
#  Example 1: 
# 
#  
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false 
#  Related Topics 数组 二分查找 
#  👍 215 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        left, right = 0, len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            element = matrix[mid // len(matrix[0])][mid % len(matrix[0])]
            if element == target: return True
            elif element < target: left = mid + 1
            else: right = mid - 1
        return False
# leetcode submit region end(Prohibit modification and deletion)
