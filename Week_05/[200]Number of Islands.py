# Given a 2d grid map of '1's (land) and '0's (water), count the number of islan
# ds. An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all su
# rrounded by water. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 704 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # UnionFind Solution
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        self.count = sum(grid[i][j] == '1' for i in range(m) for j in range(n))
        parent = list(range(m * n))
        rank = [0] * (m * n)

        def find(x):
            root = x
            while parent[root] != root:
                root = parent[root]
            while parent[x] != x:
                parent[x], x = root, parent[x]
            return root

        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot: return
            if rank[xroot] < rank[yroot]:
                xroot, yroot = yroot, xroot
            parent[yroot] = xroot
            rank[xroot] = max(rank[xroot], rank[yroot] + 1)
            self.count -= 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    curr = i * n + j
                    if j + 1 < n and grid[i][j + 1] == '1': union(curr, curr + 1)
                    if i + 1 < m and grid[i + 1][j] == '1': union(curr, curr + n)
        return self.count
# leetcode submit region end(Prohibit modification and deletion)
S = Solution()
S.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])