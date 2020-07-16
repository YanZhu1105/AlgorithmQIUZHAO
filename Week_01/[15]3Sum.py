# Given an array nums of n integers, are there elements a, b, c in nums such tha
# t a + b + c = 0? Find all unique triplets in the array which gives the sum of ze
# ro. 
# 
#  Note: 
# 
#  The solution set must not contain duplicate triplets. 
# 
#  Example: 
# 
#  
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#  
#  Related Topics 数组 双指针 
#  👍 2373 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # two pointers
    def threeSum_twoPointer(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3: return []
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if nums[i] > 0: return res
            if i > 0 and nums[i] == nums[i - 1]: continue

            L, R = i + 1, len(nums) - 1

            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L + 1] == nums[L]: L += 1
                    while L < R and nums[R - 1] == nums[R]: R -= 1
                    L += 1
                    R -= 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                else:
                    L += 1

        return res

    # Using set to remove duplicate
    # Similar approach as twoSum problem, just loop over the twoSum solution
    def threeSum_Set(self, nums):
        if len(nums) < 3: return []
        nums.sort()
        res = set()

        for i, num in enumerate(nums[:-2]):
            if num > 0: break
            if i > 0 and num == nums[i - 1]: continue

            tmp = {}
            for right in nums[i + 1:]:
                if right not in tmp:
                    tmp[-num-right] = "无所谓是啥"
                else:
                    res.add((num, -num-right, right))

        return list(res)


# leetcode submit region end(Prohibit modification and deletion)
