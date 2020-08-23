# Given a string, you need to reverse the order of characters in each word withi
# n a sentence while still preserving whitespace and initial word order. 
# 
#  Example 1: 
#  
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#  
#  
# 
#  Note:
# In the string, each word is separated by single space and there will not be an
# y extra space in the string.
#  Related Topics 字符串 
#  👍 216 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])[::-1]
# leetcode submit region end(Prohibit modification and deletion)
