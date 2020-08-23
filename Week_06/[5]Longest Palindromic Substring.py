# Given a string s, find the longest palindromic substring in s. You may assume 
# that the maximum length of s is 1000. 
# 
#  Example 1: 
# 
#  
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#  
# 
#  Example 2: 
# 
#  
# Input: "cbbd"
# Output: "bb"
#  
#  Related Topics 字符串 动态规划 
#  👍 2602 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        for j in range(1, size):
            for i in range(0, j):
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1])
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]
# leetcode submit region end(Prohibit modification and deletion)
