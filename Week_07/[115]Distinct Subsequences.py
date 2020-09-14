# Given a string S and a string T, count the number of distinct subsequences of 
# S which equals T. 
# 
#  A subsequence of a string is a new string which is formed from the original s
# tring by deleting some (can be none) of the characters without disturbing the re
# lative positions of the remaining characters. (ie, "ACE" is a subsequence of "AB
# CDE" while "AEC" is not). 
# 
#  It's guaranteed the answer fits on a 32-bit signed integer. 
# 
#  Example 1: 
# 
#  
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
# 
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
#  
# 
#  Example 2: 
# 
#  
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
# 
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^
#  
#  Related Topics 字符串 动态规划 
#  👍 246 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s: return 0
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

        for i in range(len(s)+1):
            dp[i][0] = 1

        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

# leetcode submit region end(Prohibit modification and deletion)
