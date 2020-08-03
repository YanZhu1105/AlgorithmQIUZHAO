# Say you have an array for which the ith element is the price of a given stock 
# on day i. 
# 
#  Design an algorithm to find the maximum profit. You may complete at most two 
# transactions. 
# 
#  Note: You may not engage in multiple transactions at the same time (i.e., you
#  must sell the stock before you buy again). 
# 
#  Example 1: 
# 
#  
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 
# 3-0 = 3.
#              Then buy on day 7 (price = 1) and sell on day 8 (price = 4), prof
# it = 4-1 = 3. 
# 
#  Example 2: 
# 
#  
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 
# 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them lat
# er, as you are
#              engaging multiple transactions at the same time. You must sell be
# fore buying again.
#  
# 
#  Example 3: 
# 
#  
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0. 
#  Related Topics 数组 动态规划 
#  👍 461 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        dp = [[[0, 0] for _ in range(3)] for _ in range(len(prices))]
        dp[0][2][0] = 0
        dp[0][2][1] = -prices[0]
        dp[0][1][0] = 0
        dp[0][1][1] = -prices[0]

        for i in range(1, len(prices)):
            # k的遍历，正序倒序没有区别，反正是相互独立的，而且都是用i - 1时候的dp值罢了
            for k in range(1, 3):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[-1][2][0]
# leetcode submit region end(Prohibit modification and deletion)
S = Solution()
S.maxProfit([3,3,5,0,0,3,1,4])
