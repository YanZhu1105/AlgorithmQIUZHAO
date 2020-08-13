# Write a program to solve a Sudoku puzzle by filling the empty cells. 
# 
#  A sudoku solution must satisfy all of the following rules: 
# 
#  
#  Each of the digits 1-9 must occur exactly once in each row. 
#  Each of the digits 1-9 must occur exactly once in each column. 
#  Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-b
# oxes of the grid. 
#  
# 
#  Empty cells are indicated by the character '.'. 
# 
#  
# A sudoku puzzle... 
# 
#  
# ...and its solution numbers marked in red. 
# 
#  Note: 
# 
#  
#  The given board contain only digits 1-9 and the character '.'. 
#  You may assume that the given Sudoku puzzle will have a single unique solutio
# n. 
#  The given board size is always 9x9. 
#  
#  Related Topics 哈希表 回溯算法 
#  👍 492 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 普通解法
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        block = [set(range(1, 10)) for _ in range(9)]
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    row[i].discard(val), col[j].discard(val), block[(i//3)*3 + j//3].discard(val)
                else:
                    empty.append((i, j))

        def backtrack(count = 0):
            if count == len(empty): return True
            i, j = empty[count]
            for val in row[i] & col[j] & block[(i//3)*3 + j//3]:
                board[i][j] = str(val)
                row[i].discard(val), col[j].discard(val), block[(i // 3) * 3 + j // 3].discard(val)
                if backtrack(count + 1): return True
                row[i].add(val), col[j].add(val), block[(i // 3) * 3 + j // 3].add(val)
        backtrack()

    # A Star
    def solveSudoku_a_star(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        from heapq import heappop, heappush
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        block = [set(range(1, 10)) for _ in range(9)]
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    row[i].discard(val), col[j].discard(val), block[(i//3)*3 + j//3].discard(val)
                else:
                    empty.append((i, j))

        def backtrack(count = 0):
            if count == len(empty): return True
            i, j = empty[count]
            for val in row[i] & col[j] & block[(i//3)*3 + j//3]:
                board[i][j] = str(val)
                row[i].discard(val), col[j].discard(val), block[(i // 3) * 3 + j // 3].discard(val)
                if backtrack(count + 1): return True
                row[i].add(val), col[j].add(val), block[(i // 3) * 3 + j // 3].add(val)
        backtrack()
# leetcode submit region end(Prohibit modification and deletion)
