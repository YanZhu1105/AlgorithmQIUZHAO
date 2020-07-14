# Given n non-negative integers a1, a2, ..., an , where each represents a point 
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
#  line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis for
# ms a container, such that the container contains the most water. 
# 
#  Note: You may not slant the container and n is at least 2. 
# 
#  
# 
#  
# 
#  The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In thi
# s case, the max area of water (blue section) the container can contain is 49. 
# 
#  
# 
#  Example: 
# 
#  
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49 Related Topics 数组 双指针 
#  👍 1631 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) == 1: return 0

        i, j = 0, len(height) - 1
        max_ = 0
        while i < j:
            if height[i] < height[j]:
                tmp = height[i] * (j - i)
                i += 1
            else:
                tmp = height[j] * (j - i)
                j -= 1
            max_ = max(max_, tmp)

        return max_
# leetcode submit region end(Prohibit modification and deletion)
