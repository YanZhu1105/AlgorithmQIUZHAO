# The n-queens puzzle is the problem of placing n queens on an n×n chessboard su
# ch that no two queens attack each other. 
# 
#  
# 
#  Given an integer n, return all distinct solutions to the n-queens puzzle. 
# 
#  Each solution contains a distinct board configuration of the n-queens' placem
# ent, where 'Q' and '.' both indicate a queen and an empty space respectively. 
# 
#  Example: 
# 
#  
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as show
# n above.
#  
#  Related Topics 回溯算法 
#  👍 475 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res, self.size = [], n
        self.dfs([], [], [])
        return [["."*col + "Q" + "."*(n-col-1) for col in sol] for sol in self.res]

    def dfs(self, path, sum_, diff_):
        row = len(path)
        if row == self.size:
            self.res.append(path[:])
            return

        for col in range(self.size):
            if col not in path and row + col not in sum_ and row - col not in diff_:
                self.dfs(path + [col], sum_ + [row + col], diff_ + [row - col])
# leetcode submit region end(Prohibit modification and deletion)

