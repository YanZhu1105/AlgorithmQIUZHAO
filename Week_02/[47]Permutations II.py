# Given a collection of numbers that might contain duplicates, return all possib
# le unique permutations. 
# 
#  Example: 
# 
#  
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
#  
#  Related Topics 回溯算法 
#  👍 355 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 这题可以用swap的想法，比较巧妙，但思路还是递归回朔

    # 额外O(N)空间，但是更清楚，几乎可以当模板
    def permuteUniqueStandard(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def helper(path):
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    path.append(nums[i])
                    used[i] = True
                    helper(path)
                    path.pop()
                    used[i] = False

        if not nums: return []
        res, n = [], len(nums)
        nums.sort()
        used = [False for _ in range(len(nums))]
        helper([])
        return res

    # O(1)空间，用过的元素直接砍掉，没有之前那么逻辑清晰
    def permuteUniqueRemove(self, nums):
        def helper(path, nums):
            if not nums:
                res.append(path[:])
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                helper(path + [nums[i]], nums[:i] + nums[i + 1:])

        res = []
        nums.sort()
        helper([], nums)
        return res

# leetcode submit region end(Prohibit modification and deletion)
