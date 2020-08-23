# Given a string, determine if it is a palindrome, considering only alphanumeric
#  characters and ignoring cases. 
# 
#  Note: For the purpose of this problem, we define empty string as valid palind
# rome. 
# 
#  Example 1: 
# 
#  
# Input: "A man, a plan, a canal: Panama"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: "race a car"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  s consists only of printable ASCII characters. 
#  
#  Related Topics 双指针 字符串 
#  👍 264 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sgood = ''.join(char.lower()for char in s if char.isalnum())
        return sgood == sgood[::-1]
# leetcode submit region end(Prohibit modification and deletion)
