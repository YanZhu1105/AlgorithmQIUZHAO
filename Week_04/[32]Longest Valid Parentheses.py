# Given a string containing just the characters '(' and ')', find the length of 
# the longest valid (well-formed) parentheses substring. 
# 
#  Example 1: 
# 
#  
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
#  
# 
#  Example 2: 
# 
#  
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
#  
#  Related Topics 字符串 动态规划 
#  👍 887 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp定义：以当前index为结束的最长有效括号数
        # 状态转移方程：若是左括号，那么就是0，若是右括号，前一个是左括号，就是dp[i-2] + 2, 前一个还是右括号，
        # 就要去i-1再减去dp[i-1]个位置看，是左括号的话，顺利凑成一对，不然没有。注意要判断边界，都要 >= 0
        # 初始值 dp[0] = 0, dp[1]就看前两个是不是一对
        if len(s) <= 1: return 0
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(': dp[i] = dp[i-2] + 2
                else:
                    if s[i-1-dp[i-1]] == '(' and i-1-dp[i-1] >= 0:
                        dp[i] = dp[i-1] + (dp[i-1-dp[i-1]-1] if i-1-dp[i-1]-1 >= 0 else 0) + 2
        return max(dp)
# leetcode submit region end(Prohibit modification and deletion)
S = Solution()
S.longestValidParentheses('(()))())(')