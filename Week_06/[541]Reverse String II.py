# 
# Given a string and an integer k, you need to reverse the first k characters fo
# r every 2k characters counting from the start of the string. If there are less t
# han k characters left, reverse all of them. If there are less than 2k but greate
# r than or equal to k characters, then reverse the first k characters and left th
# e other as original.
#  
# 
#  Example: 
#  
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
#  
#  
# 
# Restrictions: 
#  
#  The string consists of lower English letters only. 
#  Length of the given string and k will in the range [1, 10000] 
#  Related Topics 字符串 
#  👍 87 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)
        
# leetcode submit region end(Prohibit modification and deletion)
S = Solution()
S.reverseStr(s = "abcdefg", k = 2)
