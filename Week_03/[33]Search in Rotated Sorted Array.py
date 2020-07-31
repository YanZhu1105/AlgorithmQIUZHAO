# Suppose an array sorted in ascending order is rotated at some pivot unknown to
#  you beforehand. 
# 
#  (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]). 
# 
#  You are given a target value to search. If found in the array return its inde
# x, otherwise return -1. 
# 
#  You may assume no duplicate exists in the array. 
# 
#  Your algorithm's runtime complexity must be in the order of O(log n). 
# 
#  Example 1: 
# 
#  
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1 
#  Related Topics 数组 二分查找 
#  👍 853 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 总结上面向前规约的三种情况：
            # 1. nums[0] <= target < nums[mid]
            # 2. target < nums[mid] < nums[0]
            # 3.  nums[mid] < nums[0] <= target
            # 这三个是互斥的，同时只要有一个为真则向前规约
            # 如下：
            if nums[0] <= target < nums[mid] or target < nums[mid] < nums[0] or nums[mid] < nums[0] <= target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
# leetcode submit region end(Prohibit modification and deletion)
