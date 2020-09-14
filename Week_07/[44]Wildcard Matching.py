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
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = '?' + s
        p = '?' + p
        ls, lp = len(s), len(p)

        dp = [[False] * (ls) for _ in range(lp)]
        dp[0][0] = True

        for i in range(1, lp):
            if p[i] == "*":
                for j in range(ls):
                    dp[i][j] = True
            else:
                break

        for i in range(1, lp):
            for j in range(1, ls):
                if p[i] == '*':
                    if dp[i - 1][j] or dp[i][j - 1]:
                        dp[i][j] = True

                elif p[i] == "?" or p[i] == s[j]:
                    dp[i][j] = dp[i - 1][j - 1]
        # return dp
        return dp[lp - 1][ls - 1]

# leetcode submit region end(Prohibit modification and deletion)
