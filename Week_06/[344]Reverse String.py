# Write a function that reverses a string. The input string is given as an array
#  of characters char[]. 
# 
#  Do not allocate extra space for another array, you must do this by modifying 
# the input array in-place with O(1) extra memory. 
# 
#  You may assume all the characters consist of printable ascii characters. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#  
#  
#  
#  Related Topics 双指针 字符串 
#  👍 270 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
# leetcode submit region end(Prohibit modification and deletion)
