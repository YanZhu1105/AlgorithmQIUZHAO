# English description is not available for the problem. Please switch to Chinese
# . Related Topics 堆 分治算法 
#  👍 107 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    import heapq
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []

        for num in arr:
            num = -num
            if len(res) < k:
                heapq.heappush(res, num)
            else:
                heapq.heappushpop(res, num)

        return [-x for x in res]


# leetcode submit region end(Prohibit modification and deletion)
