# Given a non-empty array of digits representing a non-negative integer, increme
# nt one to the integer. 
# 
#  The digits are stored such that the most significant digit is at the head of 
# the list, and each element in the array contains a single digit. 
# 
#  You may assume the integer does not contain any leading zero, except the numb
# er 0 itself. 
# 
#  Example 1: 
# 
#  
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#  
# 
#  Example 2: 
# 
#  
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#  
#  Related Topics 数组 
#  👍 500 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits
# leetcode submit region end(Prohibit modification and deletion)
