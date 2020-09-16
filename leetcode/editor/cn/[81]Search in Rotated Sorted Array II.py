# Suppose an array sorted in ascending order is rotated at some pivot unknown to
#  you beforehand. 
# 
#  (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]). 
# 
#  You are given a target value to search. If found in the array return true, ot
# herwise return false. 
# 
#  Example 1: 
# 
#  
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false 
# 
#  Follow up: 
# 
#  
#  This is a follow up problem to Search in Rotated Sorted Array, where nums may
#  contain duplicates. 
#  Would this affect the run-time complexity? How and why? 
#  
#  Related Topics 数组 二分查找 
#  👍 215 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target: return True
            while l < mid and nums[l] == nums[mid]: l += 1
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
# leetcode submit region end(Prohibit modification and deletion)
