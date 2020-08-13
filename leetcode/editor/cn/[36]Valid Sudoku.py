# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be val
# idated according to the following rules: 
# 
#  
#  Each row must contain the digits 1-9 without repetition. 
#  Each column must contain the digits 1-9 without repetition. 
#  Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without r
# epetition. 
#  
# 
#  
# A partially filled sudoku which is valid. 
# 
#  The Sudoku board could be partially filled, where empty cells are filled with
#  the character '.'. 
# 
#  Example 1: 
# 
#  
# Input:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being
#  
#     modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is 
# invalid.
#  
# 
#  Note: 
# 
#  
#  A Sudoku board (partially filled) could be valid but is not necessarily solva
# ble. 
#  Only the filled cells need to be validated according to the mentioned rules. 
# 
#  The given board contain only digits 1-9 and the character '.'. 
#  The given board size is always 9x9. 
#  
#  Related Topics 哈希表 
#  👍 391 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = len(board)
        row = [set() for _ in range(n)]
        col = [set() for _ in range(n)]
        sec = [set() for _ in range(9)]
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.': continue
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in sec[(i // 3) * 3 + j // 3]:
                    return False
                row[i].add(board[i][j]); col[j].add(board[i][j]); sec[(i // 3) * 3 + j // 3].add(board[i][j])
        return True
# leetcode submit region end(Prohibit modification and deletion)
