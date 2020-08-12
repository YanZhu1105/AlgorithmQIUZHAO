# The n-queens puzzle is the problem of placing n queens on an n×n chessboard su
# ch that no two queens attack each other. 
# 
#  
# 
#  Given an integer n, return the number of distinct solutions to the n-queens p
# uzzle. 
# 
#  Example: 
# 
#  
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown 
# below.
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#  
#  Related Topics 回溯算法 
#  👍 140 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        self.res = 0
        self.dfs(0, 0, 0, 0)
        return self.res

    def dfs(self, row, cols, xy_dif, xy_sum):
        if row >= self.n:
            self.res += 1
            return
        bits = (~(cols | xy_dif | xy_sum) & ((1 << self.n) - 1))  # 得到所有空位，也就是1
        print(f'row = {row}, cols = {bin(cols)}, xy_dif = {bin(xy_dif)}, xy_sum = {bin(xy_sum)}, bits = {bin(bits)}')
        while bits:
            p = bits & -bits  # 取到最低位的1
            bits &= (bits - 1)  # 清空最低位的1，表示把皇后放在该位置
            self.dfs(row + 1, cols | p, (xy_dif | p) << 1, (xy_sum | p) >> 1)
# leetcode submit region end(Prohibit modification and deletion)
S = Solution()
S.totalNQueens(n = 4)
