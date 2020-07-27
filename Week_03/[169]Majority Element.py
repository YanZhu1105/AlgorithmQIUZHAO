# Given an array of size n, find the majority element. The majority element is t
# he element that appears more than ⌊ n/2 ⌋ times. 
# 
#  You may assume that the array is non-empty and the majority element always ex
# ist in the array. 
# 
#  Example 1: 
# 
#  
# Input: [3,2,3]
# Output: 3 
# 
#  Example 2: 
# 
#  
# Input: [2,2,1,1,1,2,2]
# Output: 2
#  
#  Related Topics 位运算 数组 分治算法 
#  👍 677 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 投票算法
    def majorityElementVote(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if candidate == num else -1)
        return candidate

    # 分治
    def majorityElementRecursion(self, nums):
        def helper(low, high):
            if low == high: return nums[low]

            mid = (low + high)//2
            left = helper(low, mid)
            right = helper(mid+1, high)

            if left == right: return left

            left_count = sum(1 for i in range(low, mid+1) if nums[i] == left)
            right_count = sum(1 for i in range(mid, high+1) if nums[i] == right)

            return left if left_count > right_count else right
        return helper(0, len(nums)-1)
# leetcode submit region end(Prohibit modification and deletion)
