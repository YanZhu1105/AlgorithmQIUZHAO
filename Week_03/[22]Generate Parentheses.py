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
#  👍 1195 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateParenthesisDFS(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(left, right, path):
            if left == right == 0: res.append(path[:])
            if left > 0: helper(left-1, right, path + '(')
            if right > left: helper(left, right-1, path + ')')
        res = []
        helper(n, n, '')
        return res

    def generateParenthesisBFS(self, n):
        res, queue = [], collections.deque()
        queue.append(('', n, n))
        while queue:
            path, left, right = queue.popleft()
            if left == right == 0:
                res.append(path)
                continue
            if left > 0:
                queue.append((path + '(', left - 1, right))
            if right > left:
                queue.append((path + ')', left, right - 1))
        return res

# leetcode submit region end(Prohibit modification and deletion)
