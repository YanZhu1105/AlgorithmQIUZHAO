# Given a string s consists of upper/lower-case alphabets and empty space charac
# ters ' ', return the length of last word (last word means the last appearing wor
# d if we loop from left to right) in the string. 
# 
#  If the last word does not exist, return 0. 
# 
#  Note: A word is defined as a maximal substring consisting of non-space charac
# ters only. 
# 
#  Example: 
# 
#  
# Input: "Hello World"
# Output: 5
#  
# 
#  
#  Related Topics 字符串 
#  👍 237 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' and count == 0: continue
            if s[i] == ' ': return count
            count += 1
        return count
# leetcode submit region end(Prohibit modification and deletion)
