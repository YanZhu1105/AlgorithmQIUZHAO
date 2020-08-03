# Say you have an array for which the i-th element is the price of a given stock
#  on day i. 
# 
#  Design an algorithm to find the maximum profit. You may complete at most k tr
# ansactions. 
# 
#  Note: 
# You may not engage in multiple transactions at the same time (ie, you must sel
# l the stock before you buy again). 
# 
#  Example 1: 
# 
#  
# Input: [2,4,1], k = 2
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 
# 4-2 = 2.
#  
# 
#  Example 2: 
# 
#  
# Input: [3,2,6,5,0,3], k = 2
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 
# 6-2 = 4.
#              Then buy on day 5 (price = 0) and sell on day 6 (price = 3), prof
# it = 3-0 = 3.
#  
#  Related Topics 动态规划 
#  👍 259 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k > len(prices)//2:
            profit = 0
            for i, price in enumerate(prices):
                if i > 0 and price > prices[i - 1]:
                    profit += price - prices[i - 1]
            return profit

        maxk = k
        if not prices: return 0
        dp = [[[0, 0] for _ in range(maxk + 1)] for _ in range(len(prices))]

        for i in range(len(prices)):
            # k的遍历，正序倒序没有区别，反正是相互独立的，而且都是用i - 1时候的dp值罢了
            for k in range(1, maxk + 1):
                if i == 0:
                    dp[0][k][0] = 0
                    dp[0][k][1] = -prices[0]
                else:
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[-1][maxk][0]
# leetcode submit region end(Prohibit modification and deletion)
