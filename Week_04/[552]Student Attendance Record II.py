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
class Solution:
    def checkRecord(self, n: int) -> int:
        # 6 possiblity:
        # 1. no A, end in P
        # 2. no A, end in 1L
        # 3. no A, end in 2L
        # 4. A, end in P/A
        # 5. A, end in 1L
        # 6. A, end in 2L

        count, m = [1, 1, 0, 1, 0, 0], 10 ** 9 + 7
        for _ in range(1, n):
            without_A, with_A = sum(count[:3]) % m, sum(count[3:]) % m
            # 解释：
            # 1. 之前没有A，随便啥结尾，现在加个P
            # 2. 之前没有A，并且P结尾，现在加个L
            # 3. 之前没有A，并且1个L结尾，现在加个L
            # 4. 有A，分两种，之前有A，现在加P，之前没A，现在加A
            # 5. 之前有A，现在加L
            # 6. 之前有A, 并且1个L结尾，现在加个L
            count = [without_A, count[0], count[1], without_A + with_A, count[3], count[4]]
        return sum(count) % m
# leetcode submit region end(Prohibit modification and deletion)
