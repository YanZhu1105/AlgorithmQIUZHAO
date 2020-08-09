# Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rec
# tangle in the matrix such that its sum is no larger than k. 
# 
#  Example: 
# 
#  
# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2 
# Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
#              and 2 is the max number no larger than k (k = 2). 
# 
#  Note: 
# 
#  
#  The rectangle inside the matrix must have an area > 0. 
#  What if the number of rows is much larger than the number of columns? 
#  Related Topics 队列 二分查找 动态规划 
#  👍 111 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import bisect
        row, col = len(matrix), len(matrix[0])
        res = float('-inf')
        for left in range(col):
            _sum = [0] * row
            for right in range(left, col):
                for j in range(row):
                    _sum[j] += matrix[j][right]
                arr, cur = [0], 0
                for tmp in _sum:
                    cur += tmp
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr): res = max(cur - arr[loc], res)
                    # 把累加和加入
                    bisect.insort(arr, cur)
        return res
# leetcode submit region end(Prohibit modification and deletion)
