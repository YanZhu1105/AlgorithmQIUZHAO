# You are climbing a stair case. It takes n steps to reach to the top. 
# 
#  Each time you can either climb 1 or 2 steps. In how many distinct ways can yo
# u climb to the top? 
# 
#  Example 1: 
# 
#  
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#  
# 
#  Example 2: 
# 
#  
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 45 
#  
#  Related Topics 动态规划 
#  👍 1168 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 可以爬1，2，3层
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in (1, 2): return n
        if n == 3: return 4

        f1, f2, f3 = 1, 2, 4

        for _ in range(4, n+1):
            f = f1 + f2 + f3
            f1, f2, f3 = f2, f3, f
        return f

    # 相邻两步不能相同
    def climbStairsDifferentStep(self, n):
        if n in (1, 2): return n
        if n == 3: return 4
        dp = [[0 for _ in range(4)] for _ in range(n+1)]
        # row是当前层数，col是到达当前层最后一步跨的是哪种，值是多少种爬法
        dp[3][3] = 1
        dp[3][2] = dp[1][1] = 1
        dp[3][1] = dp[2][2] = 1
        for i in range(4, n+1):
            dp[i][1] = dp[i-1][2] + dp[i-1][3]
            dp[i][2] = dp[i-2][1] + dp[i-2][3]
            dp[i][3] = dp[i-3][1] + dp[i-3][2]
        return dp[-1][1] + dp[-1][2] + dp[-1][3]
# leetcode submit region end(Prohibit modification and deletion)

S = Solution()
S.climbStairsDifferentStep(5)
