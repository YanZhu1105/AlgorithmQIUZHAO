# In an N by N square grid, each cell is either empty (0) or blocked (1). 
# 
#  A clear path from top-left to bottom-right has length k if and only if it is 
# composed of cells C_1, C_2, ..., C_k such that: 
# 
#  
#  Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are d
# ifferent and share an edge or corner) 
#  C_1 is at location (0, 0) (ie. has value grid[0][0]) 
#  C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1]) 
#  If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0). 
# 
#  
# 
#  Return the length of the shortest such clear path from top-left to bottom-rig
# ht. If such a path does not exist, return -1. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [[0,1],[1,0]]
# 
# 
# Output: 2
# 
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [[0,0,0],[1,1,0],[1,1,0]]
# 
# 
# Output: 4
# 
#  
# 
#  
#  
# 
#  Note: 
# 
#  
#  1 <= grid.length == grid[0].length <= 100 
#  grid[r][c] is 0 or 1 
#  
#  Related Topics 广度优先搜索 
#  👍 55 👎 0


# leetcode submit region begin(Prohibit modification and deletion)


from heapq import heappop, heappush
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or grid[-1][-1] == 1 or grid[0][0] == 1: return -1
        pq, n, visited = [], len(grid), set()
        if n <= 2: return n
        heappush(pq, (2*n, 0, 0, 1))
        while pq:
            _, i, j, step = heappop(pq)
            if (i, j) in visited: continue
            visited.add((i, j))
            for di, dj in ((1, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (0, 1), (0, -1), (-1, 1)):
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < n and 0 <= new_j < n and not grid[new_i][new_j]:
                    if new_i == new_j == n - 1:
                        return step + 1
                    heappush(pq, (self.manhattan(new_i, new_j, n) + step, new_i, new_j, step + 1))

        return -1
    def manhattan(self, x, y, n):
        return max(abs(n - 1 - x), abs(n - 1 - y))
# leetcode submit region end(Prohibit modification and deletion)
S = Solution()
S.shortestPathBinaryMatrix([[0,0,0,0,0,0,0,0,0],[0,1,1,0,0,0,0,0,0],[1,0,0,1,0,0,0,0,0],[0,1,0,0,1,1,0,0,1],[0,0,1,0,0,1,0,0,1],[0,1,0,1,0,0,1,1,0],[0,0,0,0,0,1,0,0,0],[0,1,0,1,0,0,1,0,0],[0,1,1,0,0,0,0,1,0]])