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
#  👍 1172 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateParenthesis(self, n: int):
        def helper(left, right, path, level):
            if right == 0:
                res.append(path[:])
                return

            if left > 0:
                path += '('
                print(f'level = {level}, {path}')
                level += 1
                helper(left - 1, right, path, level)
                level -= 1
                path = path[:-1]

            if right > left:
                path += ')'
                print(f'level = {level}, {path}')
                level += 1
                helper(left, right - 1, path, level)
                level -= 1



        res = []
        helper(n, n, '', level = 1)
        return res

if __name__ == '__main__':
    S = Solution()
    S.generateParenthesis(3)

# leetcode submit region end(Prohibit modification and deletion)
