# Implement pow(x, n), which calculates x raised to the power n (xn). 
# 
#  Example 1: 
# 
#  
# Input: 2.00000, 10
# Output: 1024.00000
#  
# 
#  Example 2: 
# 
#  
# Input: 2.10000, 3
# Output: 9.26100
#  
# 
#  Example 3: 
# 
#  
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
#  
# 
#  Note: 
# 
#  
#  -100.0 < x < 100.0 
#  n is a 32-bit signed integer, within the range [−231, 231 − 1] 
#  
#  Related Topics 数学 二分查找 
#  👍 453 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def helper(n):
            if n == 0:
                return 1
            y = helper(n//2)
            return y*y if n%2 == 0 else y*y*x

        return helper(n) if n > 0 else 1/helper(-n)

# leetcode submit region end(Prohibit modification and deletion)
