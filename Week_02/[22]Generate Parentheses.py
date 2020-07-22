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
#  👍 1176 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def helper(left, right, path):
            if not left and not right:
                res.append(path[:])
                return

            if left > 0:
                helper(left - 1, right, path + '(')
            if left < right:
                helper(left, right - 1, path + ')')

        res = []
        helper(n, n, '')
        return res
# leetcode submit region end(Prohibit modification and deletion)
