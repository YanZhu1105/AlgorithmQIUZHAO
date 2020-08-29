# Given an input string (s) and a pattern (p), implement regular expression matc
# hing with support for '.' and '*'. 
# 
#  
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#  
# 
#  The matching should cover the entire input string (not partial). 
# 
#  Note: 
# 
#  
#  s could be empty and contains only lowercase letters a-z. 
#  p could be empty and contains only lowercase letters a-z, and characters like
#  . or *. 
#  
# 
#  Example 1: 
# 
#  
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#  
# 
#  Example 2: 
# 
#  
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, 
# by repeating 'a' once, it becomes "aa".
#  
# 
#  Example 3: 
# 
#  
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#  
# 
#  Example 4: 
# 
#  
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, i
# t matches "aab".
#  
# 
#  Example 5: 
# 
#  
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
#  
#  Related Topics 字符串 动态规划 回溯算法 
#  👍 1488 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)

        def matches(i, j):
            return (i != 0) and (p[j - 1] in ['.', s[i - 1]])

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # f[i][j] |= f[i][j - 2]
                    # if matches(i, j - 1):
                    f[i][j] |= f[i - 1][j] & matches(i, j - 1) | f[i][j - 2]
                else:
                    # if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1] & matches(i, j)
        return f[m][n]

# leetcode submit region end(Prohibit modification and deletion)
