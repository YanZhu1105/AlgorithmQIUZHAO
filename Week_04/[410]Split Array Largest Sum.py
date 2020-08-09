# Given an array which consists of non-negative integers and an integer m, you c
# an split the array into m non-empty continuous subarrays. Write an algorithm to 
# minimize the largest sum among these m subarrays.
#  
# 
#  Note: 
# If n is the length of array, assume the following constraints are satisfied:
#  
#  1 ≤ n ≤ 1000 
#  1 ≤ m ≤ min(50, n) 
#  
#  
# 
#  Examples: 
#  
# Input:
# nums = [7,2,5,10,8]
# m = 2
# 
# Output:
# 18
# 
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
#  
#  Related Topics 二分查找 动态规划 
#  👍 301 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def check(x):
            total, count = 0, 1
            for num in nums:
                if total + num > x:
                    count += 1
                    total = num
                else:
                    total += num
            return count <= m
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
        
# leetcode submit region end(Prohibit modification and deletion)
