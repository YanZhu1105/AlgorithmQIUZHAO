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
#  👍 1128 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        if n == 2: return 2

        first, second = 1, 2

        for _ in range(3, n+1):
            third = first + second
            first, second = second, third

        return third
# leetcode submit region end(Prohibit modification and deletion)
