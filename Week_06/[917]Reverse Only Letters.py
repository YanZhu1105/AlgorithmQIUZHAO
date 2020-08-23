# Given a string S, return the "reversed" string where all characters that are n
# ot a letter stay in the same place, and all letters reverse their positions. 
# 
#  
# 
#  
#  
#  
#  
#  
#  
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: "ab-cd"
# Output: "dc-ba"
#  
# 
#  
#  Example 2: 
# 
#  
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
#  
# 
#  
#  Example 3: 
# 
#  
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#  
# 
#  
# 
#  
#  Note: 
# 
#  
#  S.length <= 100 
#  33 <= S[i].ASCIIcode <= 122 
#  S doesn't contain \ or " 
#  
#  
#  
#  
#  Related Topics 字符串 
#  👍 60 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        if not S: return ''
        i, j = 0, len(S) - 1
        while i < j:
            while i < j and not S[i].isalpha(): i += 1
            while i < j and not S[j].isalpha(): j -= 1
            S[i], S[j] = S[j], S[i]
            i += 1; j -= 1
        return ''.join(S)
# leetcode submit region end(Prohibit modification and deletion)
