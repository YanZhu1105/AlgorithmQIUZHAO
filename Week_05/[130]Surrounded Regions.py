# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions su
# rrounded by 'X'. 
# 
#  A region is captured by flipping all 'O's into 'X's in that surrounded region
# . 
# 
#  Example: 
# 
#  
# X X X X
# X O O X
# X X O X
# X O X X
#  
# 
#  After running your function, the board should be: 
# 
#  
# X X X X
# X X X X
# X X X X
# X O X X
#  
# 
#  Explanation: 
# 
#  Surrounded regions shouldn’t be on the border, which means that any 'O' on th
# e border of the board are not flipped to 'X'. Any 'O' that is not on the border 
# and it is not connected to an 'O' on the border will be flipped to 'X'. Two cell
# s are connected if they are adjacent cells connected horizontally or vertically.
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 348 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board: return
        m, n = len(board), len(board[0])
        parent = list(range(m * n + 1))
        dummy = m * n
        rank = [0] * (m * n + 1)

        def _find(x):
            root = x
            while parent[root] != root:
                root = parent[root]
            while parent[x] != x:
                parent[x], x = root, parent[x]
            return root

        def _union(x, y):
            if _find(x) == _find(y):
                return
            xroot, yroot = _find(x), _find(y)
            if rank[xroot] < rank[yroot]:
                xroot, yroot = yroot, xroot
            parent[yroot] = xroot
            rank[xroot] = max(rank[yroot] + 1, rank[xroot])

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        _union(i * n + j, dummy)
                    else:
                        for x, y in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                            if board[i + x][j + y] == 'O':
                                _union((i + x) * n + (j + y), i * n + j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and _find(dummy) != _find(i * n + j):
                    board[i][j] = 'X'
# leetcode submit region end(Prohibit modification and deletion)

S = Solution()
S.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])