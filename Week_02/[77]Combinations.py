# Given two integers n and k, return all possible combinations of k numbers out 
# of 1 ... n. 
# 
#  Example: 
# 
#  
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#  
#  Related Topics 回溯算法 
#  👍 317 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def helper(index, path):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(index, n + 1):
                helper(i + 1, path + [i])

        res = []
        helper(1, [])
        return res

    def combineListComprehension(self, n, k):
        res = [[]]
        for _ in range(k):
            res = [[i] + c for c in res for i in range(1, c[-1] if c else n + 1)]
        return res

# leetcode submit region end(Prohibit modification and deletion)
