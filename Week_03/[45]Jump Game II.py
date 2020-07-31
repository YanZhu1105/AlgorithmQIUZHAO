# Given an array of non-negative integers, you are initially positioned at the f
# irst index of the array. 
# 
#  Each element in the array represents your maximum jump length at that positio
# n. 
# 
#  Your goal is to reach the last index in the minimum number of jumps. 
# 
#  Example: 
# 
#  
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index. 
# 
#  Note: 
# 
#  You can assume that you can always reach the last index. 
#  Related Topics 贪心算法 数组 
#  👍 638 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        canReach, endPos, step = 0, 0, 0
        for i, num in enumerate(nums):
            canReach = max(canReach, i + num)
            if i == endPos:
                endPos = canReach
                step += 1
                if canReach >= len(nums)-1:
                    return step
        return 0
# leetcode submit region end(Prohibit modification and deletion)
