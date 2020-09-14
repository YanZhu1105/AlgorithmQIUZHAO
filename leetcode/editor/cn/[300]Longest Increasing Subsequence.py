# Given an unsorted array of integers, find the length of longest increasing sub
# sequence. 
# 
#  Example: 
# 
#  
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the 
# length is 4. 
# 
#  Note: 
# 
#  
#  There may be more than one LIS combination, it is only necessary for you to r
# eturn the length. 
#  Your algorithm should run in O(n2) complexity. 
#  
# 
#  Follow up: Could you improve it to O(n log n) time complexity? 
#  Related Topics 二分查找 动态规划 
#  👍 941 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # DP
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
# leetcode submit region end(Prohibit modification and deletion)
