# 
# Given a non-empty string s, you may delete at most one character. Judge whethe
# r you can make it a palindrome.
#  
# 
#  Example 1: 
#  
# Input: "aba"
# Output: True
#  
#  
# 
#  Example 2: 
#  
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
#  
#  
# 
#  Note: 
#  
#  The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000. 
#  
#  Related Topics 字符串 
#  👍 249 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isPalindrome = lambda x : x == x[::-1]
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(s[left + 1 : right + 1]) or isPalindrome(s[left: right])
        return True

# leetcode submit region end(Prohibit modification and deletion)
