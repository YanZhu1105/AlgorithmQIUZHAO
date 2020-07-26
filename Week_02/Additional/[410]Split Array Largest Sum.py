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
#  👍 234 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low + high) // 2
            total, count = 0, 0
            for num in nums:
                total += num
                if total > mid:
                    total = num
                    count += 1
            count += 1
            if count > m:
                low = mid + 1
            else:
                high = mid
        return low

# leetcode submit region end(Prohibit modification and deletion)
