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
#  👍 455 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # heap solution
    from heapq import heappush, heappop
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res, heap = [], []
        for i, num in enumerate(nums):
            heappush(heap, (-num, i))
            if i - k + 1 >= 0:
                while heap and heap[0][1] <= i - k: heappop(heap)
                res.append(-heap[0][0])

        return res
# leetcode submit region end(Prohibit modification and deletion)
