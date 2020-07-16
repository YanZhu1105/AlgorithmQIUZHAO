# Given an array nums, there is a sliding window of size k which is moving from 
# the very left of the array to the very right. You can only see the k numbers in 
# the window. Each time the sliding window moves right by one position. Return the
#  max sliding window. 
# 
#  Follow up: 
# Could you solve it in linear time? 
# 
#  Example: 
# 
#  
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7] 
# Explanation: 
# 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10^5 
#  -10^4 <= nums[i] <= 10^4 
#  1 <= k <= nums.length 
#  
#  Related Topics 堆 Sliding Window 
#  👍 450 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 可以用heap，但是需要加index，故不做考虑
    # 左右双scan有点奇技淫巧，故不做考虑
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        deque = collections.deque()

        for i in range(len(nums)):
            if deque and deque[0] <= i - k: deque.popleft()
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
            if i >= k - 1: res.append(nums[deque[0]])

        return res
# leetcode submit region end(Prohibit modification and deletion)
