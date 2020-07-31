# Given a positive integer num, write a function which returns True if num is a 
# perfect square else False. 
# 
#  Follow up: Do not use any built-in library function such as sqrt. 
# 
#  
#  Example 1: 
#  Input: num = 16
# Output: true
#  Example 2: 
#  Input: num = 14
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= num <= 2^31 - 1 
#  
#  Related Topics 数学 二分查找 
#  👍 150 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low, high = 1, num/2 + 1
        while low <= high:
            mid = (low + high)//2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                high = mid - 1
            else:
                low = mid + 1
        return False

    #NR
    def isPerfectSquareNR(self, x):
        r = x
        while r * r > x:                # 当 r*r <= x时，找到了向下取整的答案
            r = (r + x / r) / 2
        return r * r == x
# leetcode submit region end(Prohibit modification and deletion)
