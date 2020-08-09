# Given a string, your task is to count how many palindromic substrings in this 
# string. 
# 
#  The substrings with different start indexes or end indexes are counted as dif
# ferent substrings even they consist of same characters. 
# 
#  Example 1: 
# 
#  
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#  
# 
#  
# 
#  Example 2: 
# 
#  
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#  
# 
#  
# 
#  Note: 
# 
#  
#  The input string length won't exceed 1000. 
#  
# 
#  Related Topics 字符串 动态规划 
#  👍 293 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        res = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1])
                res += dp[i][j]
        return res
# leetcode submit region end(Prohibit modification and deletion)
S = Solution()
S.countSubstrings('abcbd')