# Given a positive integer n, return the number of all possible attendance recor
# ds with length n, which will be regarded as rewardable. The answer may be very l
# arge, return it after mod 109 + 7. 
# 
#  A student attendance record is a string that only contains the following thre
# e characters: 
# 
#  
#  
#  'A' : Absent. 
#  'L' : Late. 
#  'P' : Present. 
#  
#  
# 
#  
# A record is regarded as rewardable if it doesn't contain more than one 'A' (ab
# sent) or more than two continuous 'L' (late). 
# 
#  Example 1: 
#  
# Input: n = 2
# Output: 8 
# Explanation:
# There are 8 records with length 2 will be regarded as rewardable:
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" won't be regarded as rewardable owing to more than one absent times.
#  
#  
#  
# 
#  Note:
# The value of n won't exceed 100,000.
#  
# 
# 
#  Related Topics 动态规划 
#  👍 83 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """

        C, m = [1, 1, 0, 1, 0, 0], 10 ** 9 + 7
        for i in range(n - 1):
            a, b = sum(C[:3]) % m, sum(C[3:]) % m
            C = [a, C[0], C[1], a + b, C[3], C[4]]
        return sum(C) % m
# leetcode submit region end(Prohibit modification and deletion)
