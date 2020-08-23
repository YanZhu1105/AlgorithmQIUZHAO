# 
# Given n pairs of parentheses, write a function to generate all combinations of
#  well-formed parentheses.
#  
# 
#  
# For example, given n = 3, a solution set is:
#  
#  
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#  Related Topics 字符串 回溯算法 
#  👍 1254 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return []
        dp = [None for _ in range(n+1)]
        dp[0] = ['']
        for i in range(1, n + 1):
            cur = []
            for j in range(i):
                left, right = dp[j], dp[i-j-1]
                for s1 in left:
                    for s2 in right:
                        cur.append('(' + s1 + ')' + s2)
            dp[i] = cur
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
