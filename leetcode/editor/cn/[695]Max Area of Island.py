# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (r
# epresenting land) connected 4-directionally (horizontal or vertical.) You may as
# sume all four edges of the grid are surrounded by water. 
# 
#  Find the maximum area of an island in the given 2D array. (If there is no isl
# and, the maximum area is 0.) 
# 
#  Example 1: 
# 
#  
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
#  
# Given the above grid, return 6. Note the answer is not 11, because the island 
# must be connected 4-directionally.
# 
#  Example 2: 
# 
#  
# [[0,0,0,0,0,0,0,0]] 
# Given the above grid, return 0.
# 
#  Note: The length of each dimension in the given grid does not exceed 50. 
#  Related Topics 深度优先搜索 数组 
#  👍 352 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] and not visited[i][j]:
                visited[i][j] = True
                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0

        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0
# leetcode submit region end(Prohibit modification and deletion)
S = Solution()
S.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
