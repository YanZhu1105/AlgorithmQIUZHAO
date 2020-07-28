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
#  👍 676 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        def bfs(start):
            queue = collections.deque()
            queue.append(start)

            while queue:
                curr_x, curr_y = queue.popleft()
                for dx, dy in directions:
                    new_x, new_y = curr_x + dx, curr_y + dy
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and not visited[new_x][new_y] and grid[new_x][new_y] == '1':
                        queue.append((new_x, new_y))
                        visited[new_x][new_y] = True

        island = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and not visited[row][col]:
                    bfs((row, col))
                    island += 1
        return island

    # 妙阿! 对于map，filter，reduce的运用
    def numIslandsMap(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
                # for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                #     sink(x, y)
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
# leetcode submit region end(Prohibit modification and deletion)
