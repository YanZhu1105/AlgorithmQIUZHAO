# Given an integer array nums, find the contiguous subarray within an array (con
# taining at least one number) which has the largest product. 
# 
#  Example 1: 
# 
#  
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#  
# 
#  Example 2: 
# 
#  
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray. 
#  Related Topics 数组 动态规划 
#  👍 686 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        res = nums[0]  # 结果变量初始化
        # dp[i][0]存储到当前层可达到最大
        # dp[i][1]存储到当前层可达到最小
        dp = [[0] * 2 for _ in range(len(nums))]
        dp[0][0], dp[0][1] = nums[0], nums[0]
        for i in range(1, len(nums)):
            left = nums[i] * dp[i - 1][0]
            right = nums[i] * dp[i - 1][1]
            # 因为当前nums[i]可正可负，所以得到的left，right大小关系不确定
            dp[i][0] = max(left, right, nums[i])
            dp[i][1] = min(left, right, nums[i])
            res = max(res, dp[i][0])
        return res


# leetcode submit region end(Prohibit modification and deletion)
