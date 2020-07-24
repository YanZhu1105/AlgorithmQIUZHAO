# Given a collection of distinct integers, return all possible permutations. 
# 
#  Example: 
# 
#  
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#  
#  Related Topics 回溯算法 
#  👍 796 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(path, nums):
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(len(nums)):
                helper(path + [nums[i]], nums[:i] + nums[i + 1:])

        res, n = [], len(nums)
        helper([], nums)
        return res
# leetcode submit region end(Prohibit modification and deletion)
