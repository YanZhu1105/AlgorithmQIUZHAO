# Given n non-negative integers representing an elevation map where the width of
#  each bar is 1, compute how much water it is able to trap after raining. 
# 
#  
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In 
# this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos
#  for contributing this image! 
# 
#  Example: 
# 
#  
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6 
#  Related Topics 栈 数组 双指针 
#  👍 1464 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        height = [0] + height + [0]
        water = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                tmp = stack.pop()
                if not stack: continue
                h = min(height[i], height[stack[-1]]) - height[tmp]
                w = i - stack[-1] - 1
                water += h * w
            stack.append(i)

        return water

# leetcode submit region end(Prohibit modification and deletion)
