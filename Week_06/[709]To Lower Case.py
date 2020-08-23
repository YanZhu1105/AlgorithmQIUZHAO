# Implement function ToLowerCase() that has a string parameter str, and returns 
# the same string in lowercase. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: "Hello"
# Output: "hello"
#  
# 
#  
#  Example 2: 
# 
#  
# Input: "here"
# Output: "here"
#  
# 
#  
#  Example 3: 
# 
#  
# Input: "LOVELY"
# Output: "lovely"
#  
#  
#  
#  Related Topics 字符串 
#  👍 130 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        dic = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f',
               'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l',
               'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r',
               'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x',
               'Y': 'y', 'Z': 'z'}
        res = ''
        for char in str:
            if char in dic: res += dic[char]
            else: res += char
        return res
# leetcode submit region end(Prohibit modification and deletion)
