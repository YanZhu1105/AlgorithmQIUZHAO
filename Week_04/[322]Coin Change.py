# You are given coins of different denominations and a total amount of money amo
# unt. Write a function to compute the fewest number of coins that you need to mak
# e up that amount. If that amount of money cannot be made up by any combination o
# f the coins, return -1. 
# 
#  Example 1: 
# 
#  
# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1 
# 
#  Example 2: 
# 
#  
# Input: coins = [2], amount = 3
# Output: -1
#  
# 
#  Note: 
# You may assume that you have an infinite number of each kind of coin. 
#  Related Topics 动态规划 
#  👍 725 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
# leetcode submit region end(Prohibit modification and deletion)
