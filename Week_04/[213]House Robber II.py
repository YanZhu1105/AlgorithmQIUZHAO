# You are a professional robber planning to rob houses along a street. Each hous
# e has a certain amount of money stashed. All houses at this place are arranged i
# n a circle. That means the first house is the neighbor of the last one. Meanwhil
# e, adjacent houses have security system connected and it will automatically cont
# act the police if two adjacent houses were broken into on the same night. 
# 
#  Given a list of non-negative integers representing the amount of money of eac
# h house, determine the maximum amount of money you can rob tonight without alert
# ing the police. 
# 
#  Example 1: 
# 
#  
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 
# 2),
#              because they are adjacent houses.
#  
# 
#  Example 2: 
# 
#  
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4. 
#  Related Topics 动态规划 
#  👍 333 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 自己写的
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        dp = [[0]*2 for _ in range(len(nums))]
        # 0 col：必偷第一家
        dp[0][0] = nums[0]
        dp[1][0] = nums[0]
        # 1 col：必不偷第一家
        dp[0][1] = 0
        dp[1][1] = nums[1]

        for i in range(2, len(nums)-1):
            dp[i][0] = max(dp[i-2][0] + nums[i], dp[i-1][0])
        for i in range(2, len(nums)):
            dp[i][1] = max(dp[i-2][1] + nums[i], dp[i-1][1])
        return max(dp[-2][0], dp[-1][1])

    # 看了别人的，受到了启发
    def robBetter(self, nums):
        def helper(start, end):
            cur, pre = 0, 0
            for num in nums[start: end+1]:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(helper(0, len(nums)-2), helper(1, len(nums)-1)) if len(nums) != 1 else nums[0]
# leetcode submit region end(Prohibit modification and deletion)
