# Let's play the minesweeper game (Wikipedia, online game)! 
# 
#  You are given a 2D char matrix representing the game board. 'M' represents an
#  unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a re
# vealed blank square that has no adjacent (above, below, left, right, and all 4 d
# iagonals) mines, digit ('1' to '8') represents how many mines are adjacent to th
# is revealed square, and finally 'X' represents a revealed mine. 
# 
#  Now given the next click position (row and column indices) among all the unre
# vealed squares ('M' or 'E'), return the board after revealing this position acco
# rding to the following rules: 
# 
#  
#  If a mine ('M') is revealed, then the game is over - change it to 'X'. 
#  If an empty square ('E') with no adjacent mines is revealed, then change it t
# o revealed blank ('B') and all of its adjacent unrevealed squares should be reve
# aled recursively. 
#  If an empty square ('E') with at least one adjacent mine is revealed, then ch
# ange it to a digit ('1' to '8') representing the number of adjacent mines. 
#  Return the board when no more squares will be revealed. 
#  
# 
#  
# 
#  Example 1: 
# 
#  
# Input: 
# 
# [['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']]
# 
# Click : [3,0]
# 
# Output: 
# 
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
# 
# Explanation:
# 
#  
# 
#  Example 2:
# 
#  
# Input: 
# 
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
# 
# Click : [1,2]
# 
# Output: 
# 
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'X', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
# 
# Explanation:
# 
#  
# 
#  
# 
#  Note: 
# 
#  
#  The range of the input matrix's height and width is [1,50]. 
#  The click position will only be an unrevealed square ('M' or 'E'), which also
#  means the input board contains at least one clickable square. 
#  The input board won't be a stage when game is over (some mines have been reve
# aled). 
#  For simplicity, not mentioned rules should be ignored in this problem. For ex
# ample, you don't need to reveal all the unrevealed mines when the game is over, 
# consider any cases that you will win the game or flag any squares. 
#  
#  Related Topics 深度优先搜索 广度优先搜索 
#  👍 84 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def updateBoard(self, board, click):
        d = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))
        a, b = click
        if board[a][b] == 'M':
            board[a][b] = 'X'
        elif board[a][b] == 'E':
            q, m, n = {(a, b)}, len(board), len(board[0])
            while q:
                p = set()
                for i, j in q:
                    c, t = 0, []
                    for di, dj in d:
                        x, y = i + di, j + dj
                        if 0 <= x < m and 0 <= y < n:
                            c += board[x][y] == 'M'
                            board[x][y] == 'E' and t.append((x, y))   # 相当于if board[x][y] == 'E': t.append((x, y))
                    board[i][j] = c and str(c) or p.update(t) or 'B'  # 太帅了
                q = p
        return board
# leetcode submit region end(Prohibit modification and deletion)
S = Solution()
S.updateBoard([['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']], [3,0])