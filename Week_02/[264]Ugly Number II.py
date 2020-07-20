# Write a program to find the n-th ugly number. 
# 
#  Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
#  Example: 
# 
#  
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ug
# ly numbers. 
# 
#  Note: 
# 
#  
#  1 is typically treated as an ugly number. 
#  n does not exceed 1690. 
#  Related Topics 堆 数学 动态规划 
#  👍 333 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    import heapq
    #heap
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = []
        heapq.heappush(heap, 1)
        visited = set()
        visited.add(1)

        for _ in range(n):
            curr = heapq.heappop(heap)
            for num in [2, 3, 5]:
                if num * curr not in visited:
                    visited.add(num * curr)
                    heapq.heappush(heap, num * curr)

        return curr

    #DP
    def nthUglyNumberDP(self, n):
        p2, p3, p5 = 0, 0, 0
        res = [1, ]

        for _ in range(n-1):
            time2, time3, time5 = 2 * res[p2], 3 * res[p3], 5 * res[p5]
            res.append(min(time2, time3, time5))

            if res[-1] == time2: p2 += 1
            if res[-1] == time3: p3 += 1
            if res[-1] == time5: p5 += 1

        return res[-1]

# leetcode submit region end(Prohibit modification and deletion)
