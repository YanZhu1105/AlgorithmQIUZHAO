# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number
#  on it represented by array nums. You are asked to burst all the balloons. If th
# e you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Her
# e left and right are adjacent indices of i. After the burst, the left and right 
# then becomes adjacent. 
# 
#  Find the maximum coins you can collect by bursting the balloons wisely. 
# 
#  Note: 
# 
#  
#  You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can n
# ot burst them. 
#  0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100 
#  
# 
#  Example: 
# 
#  
# Input: [3,1,5,8]
# Output: 167 
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#  Related Topics 分治算法 动态规划 
#  👍 478 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        rec = [[0] * (n + 2) for _ in range(n + 2)]
        val = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += rec[i][k] + rec[k][j]
                    rec[i][j] = max(rec[i][j], total)

        return rec[0][n + 1]
# leetcode submit region end(Prohibit modification and deletion)
