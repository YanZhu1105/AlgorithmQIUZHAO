# Given an input string (s) and a pattern (p), implement wildcard pattern matchi
# ng with support for '?' and '*'. 
# 
#  
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#  
# 
#  The matching should cover the entire input string (not partial). 
# 
#  Note: 
# 
#  
#  s could be empty and contains only lowercase letters a-z. 
#  p could be empty and contains only lowercase letters a-z, and characters like
#  ? or *. 
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
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
#  
# 
#  Example 3: 
# 
#  
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not mat
# ch 'b'.
#  
# 
#  Example 4: 
# 
#  
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' ma
# tches the substring "dce".
#  
# 
#  Example 5: 
# 
#  
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false
#  
#  Related Topics 贪心算法 字符串 动态规划 回溯算法 
#  👍 502 👎 0


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
            return (i != 0) and (p[j - 1] in ['?', s[i - 1]])

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                f[0][i] = True
            else:
                break
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i - 1][j] | f[i][j - 1]
                else:
                    f[i][j] |= f[i - 1][j - 1] & matches(i, j)
        return f[m][n]
# leetcode submit region end(Prohibit modification and deletion)
