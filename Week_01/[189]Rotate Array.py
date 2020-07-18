# Given an array, rotate the array to the right by k steps, where k is non-negat
# ive. 
# 
#  Follow up: 
# 
#  
#  Try to come up as many solutions as you can, there are at least 3 different w
# ays to solve this problem. 
#  Could you do it in-place with O(1) extra space? 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 10^4 
#  It's guaranteed that nums[i] fits in a 32 bit-signed integer. 
#  k >= 0 
#  
#  Related Topics 数组 
#  👍 629 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def rotate_insert(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())

    # slicing应该已经算是用了额外空间了
    def rotate_slice(self, nums, k):
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    #采用双指针翻转，切片也行，但是用了额外空间
    def rotate_flip(self, nums, k):
        k %= len(nums)
        def flip(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        flip(nums, 0, len(nums)-1)
        flip(nums, 0, k-1)
        flip(nums, k, len(nums)-1)

    def rotate_cycle(self, nums, k):
        k %= len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start
            temp = nums[current]
            while True:
                nums[(current + k) % len(nums)], temp = temp, nums[(current + k) % len(nums)]
                current = (current + k) % len(nums)
                count += 1
                if current == start: break
            start += 1
# leetcode submit region end(Prohibit modification and deletion)
