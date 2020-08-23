# Given a collection of intervals, merge all overlapping intervals. 
# 
#  Example 1: 
# 
#  
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#  
# 
#  Example 2: 
# 
#  
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping. 
# 
#  NOTE: input types have been changed on April 15, 2019. Please reset to defaul
# t code definition to get new method signature. 
# 
#  
#  Constraints: 
# 
#  
#  intervals[i][0] <= intervals[i][1] 
#  
#  Related Topics 排序 数组 
#  👍 570 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals: return []
        intervals.sort(key = lambda x: x[0])
        res, j = [intervals[0]], 0
        for temp in intervals[1:]:
            if temp[0] > res[-1][1]:
                res.append(temp)
                j += 1
            else:
                res[j][1] = max(temp[1], res[j][1])
        return res
# leetcode submit region end(Prohibit modification and deletion)
