# Given an input string, reverse the string word by word. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: "the sky is blue"
# Output: "blue is sky the"
#  
# 
#  Example 2: 
# 
#  
# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing space
# s.
#  
# 
#  Example 3: 
# 
#  
# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single 
# space in the reversed string.
#  
# 
#  
# 
#  Note: 
# 
#  
#  A word is defined as a sequence of non-space characters. 
#  Input string may contain leading or trailing spaces. However, your reversed s
# tring should not contain leading or trailing spaces. 
#  You need to reduce multiple spaces between two words to a single space in the
#  reversed string. 
#  
# 
#  
# 
#  Follow up: 
# 
#  For C programmers, try to solve it in-place in O(1) extra space. Related Topi
# cs 字符串 
#  👍 211 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s.strip().split())
        if not s: return ''
        for i in range(len(s)//2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
        return ' '.join(s)
# leetcode submit region end(Prohibit modification and deletion)
