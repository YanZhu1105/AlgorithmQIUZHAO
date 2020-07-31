# Implement int sqrt(int x). 
# 
#  Compute and return the square root of x, where x is guaranteed to be a non-ne
# gative integer. 
# 
#  Since the return type is an integer, the decimal digits are truncated and onl
# y the integer part of the result is returned. 
# 
#  Example 1: 
# 
#  
# Input: 4
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.
#  
#  Related Topics 数学 二分查找 
#  👍 458 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # binary search
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1: return 1
        low, high = 0, x/2 + 1
        while low <= high:
            mid = (low + high)/2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid**2 > x:
                high = mid - 1
            else:
                low = mid + 1

    # NR
    def mySqrtNR(self, x):
        r = x
        while r * r > x:                # 当 r*r <= x时，找到了向下取整的答案
            r = (r + x / r) / 2
        return r
# leetcode submit region end(Prohibit modification and deletion)
