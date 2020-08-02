# Given a set of distinct integers, nums, return all possible subsets (the power
#  set). 
# 
#  Note: The solution set must not contain duplicate subsets. 
# 
#  Example: 
# 
#  
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ] 
#  Related Topics 位运算 数组 回溯算法 
#  👍 669 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 自己写的version，真丑陋
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def helper(path, size, nums):
            if len(path) == size:
                res.append(path[:])
                return

            for i in range(len(nums)):
                path.append(nums[i])
                helper(path, size, nums[i + 1:])  # nums[i + 1:]保证了当前数字和之前数字都不会再取到，防止了重复
                path.pop()

        res = []
        for i in range(len(nums) + 1):
            helper([], i, nums)
        return res

    def subsetsIteration(self, nums):
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

    def subsetsRecursion(self, nums):
        def helper(index, path):
            res.append(path)
            for i in range(index, len(nums)):
                helper(i + 1, path + [nums[i]])

        res = []
        helper(0, [])
        return res
# leetcode submit region end(Prohibit modification and deletion)
