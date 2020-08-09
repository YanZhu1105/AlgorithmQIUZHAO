# A message containing letters from A-Z is being encoded to numbers using the fo
# llowing mapping: 
# 
#  
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#  
# 
#  Given a non-empty string containing only digits, determine the total number o
# f ways to decode it. 
# 
#  Example 1: 
# 
#  
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#  
# 
#  Example 2: 
# 
#  
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6)
# . 
#  Related Topics 字符串 动态规划 
#  👍 457 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0': return 0
        if len(s) <= 1: return len(s)
        dp = [1 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] not in ('1', '2'): return 0
                else: dp[i] = dp[i-2]
            else:
                if 10 <= int(s[i-1:i+1]) <= 26: dp[i] = dp[i-1] + dp[i-2]    # 多思考一下这行
                else: dp[i] = dp[i-1]
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
S = Solution()
S.numDecodings('110')

