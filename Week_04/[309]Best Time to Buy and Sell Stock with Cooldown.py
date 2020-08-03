# Say you have an array for which the ith element is the price of a given stock 
# on day i. 
# 
#  Design an algorithm to find the maximum profit. You may complete as many tran
# sactions as you like (ie, buy one and sell one share of the stock multiple times
# ) with the following restrictions: 
# 
#  
#  You may not engage in multiple transactions at the same time (ie, you must se
# ll the stock before you buy again). 
#  After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 
# day) 
#  
# 
#  Example: 
# 
#  
# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
#  Related Topics 动态规划 
#  👍 488 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) in (0, 1): return 0
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        return dp[-1][0]

# leetcode submit region end(Prohibit modification and deletion)
