# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
#  determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  
# 
#  Note that an empty string is also considered valid. 
# 
#  Example 1: 
# 
#  
# Input: "()"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: "()[]{}"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: "(]"
# Output: false
#  
# 
#  Example 4: 
# 
#  
# Input: "([)]"
# Output: false
#  
# 
#  Example 5: 
# 
#  
# Input: "{[]}"
# Output: true
#  
#  Related Topics 栈 字符串 
#  👍 1687 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        stack = []
        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                top = stack.pop() if stack else '无所谓'
                if top != mapping[char]:
                    return False

        return not stack
# leetcode submit region end(Prohibit modification and deletion)
