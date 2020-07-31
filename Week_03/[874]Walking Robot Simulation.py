# A robot on an infinite grid starts at point (0, 0) and faces north. The robot 
# can receive one of three possible types of commands: 
# 
#  
#  -2: turn left 90 degrees 
#  -1: turn right 90 degrees 
#  1 <= x <= 9: move forward x units 
#  
# 
#  Some of the grid squares are obstacles. 
# 
#  The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1]) 
# 
#  If the robot would try to move onto them, the robot stays on the previous gri
# d square instead (but still continues following the rest of the route.) 
# 
#  Return the square of the maximum Euclidean distance that the robot will be fr
# om the origin. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: commands = [4,-1,3], obstacles = []
# Output: 25
# Explanation: robot will go to (3, 4)
#  
# 
#  
#  Example 2: 
# 
#  
# Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# Output: 65
# Explanation: robot will be stuck at (1, 4) before turning left and going to (1
# , 8)
#  
#  
# 
#  
# 
#  Note: 
# 
#  
#  0 <= commands.length <= 10000 
#  0 <= obstacles.length <= 10000 
#  -30000 <= obstacle[i][0] <= 30000 
#  -30000 <= obstacle[i][1] <= 30000 
#  The answer is guaranteed to be less than 2 ^ 31. 
#  
#  Related Topics 贪心算法 
#  👍 101 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dir = {
            'north': [0, 1, 'west', 'east'],
            'west': [-1, 0, 'south', 'north'],
            'south': [0, -1, 'east', 'west'],
            'east': [1, 0, 'north', 'south'],
        }
        face, dis, obstacles = 'north', 0, set(map(tuple, obstacles))
        x, y = 0, 0
        for cm in commands:
            if cm == -2:
                face = dir[face][2]
            elif cm == -1:
                face = dir[face][3]
            else:
                for _ in range(cm):
                    if (x + dir[face][0], y + dir[face][1]) not in obstacles:
                        x += dir[face][0]
                        y += dir[face][1]
                        dis = max(dis, x**2 + y**2)
        return dis

# leetcode submit region end(Prohibit modification and deletion)
