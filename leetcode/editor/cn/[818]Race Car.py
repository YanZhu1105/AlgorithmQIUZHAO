# Your car starts at position 0 and speed +1 on an infinite number line. (Your c
# ar can go into negative positions.) 
# 
#  Your car drives automatically according to a sequence of instructions A (acce
# lerate) and R (reverse). 
# 
#  When you get an instruction "A", your car does the following: position += spe
# ed, speed *= 2. 
# 
#  When you get an instruction "R", your car does the following: if your speed i
# s positive then speed = -1 , otherwise speed = 1. (Your position stays the same.
# ) 
# 
#  For example, after commands "AAR", your car goes to positions 0->1->3->3, and
#  your speed goes to 1->2->4->-1. 
# 
#  Now for some target position, say the length of the shortest sequence of inst
# ructions to get there. 
# 
#  
# Example 1:
# Input: 
# target = 3
# Output: 2
# Explanation: 
# The shortest instruction sequence is "AA".
# Your position goes from 0->1->3.
#  
# 
#  
# Example 2:
# Input: 
# target = 6
# Output: 5
# Explanation: 
# The shortest instruction sequence is "AAARA".
# Your position goes from 0->1->3->7->7->6.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= target <= 10000. 
#  
#  Related Topics 堆 动态规划 
#  👍 72 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    dp = {0: 0}
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target in self.dp: return self.dp[target]
        n = target.bit_length()
        if 2**n - 1 == target:
            self.dp[target] = n
        else:
            self.dp[target] = self.racecar(2**n - 1 - target) + n + 1
            for m in range(n - 1):
                self.dp[target] = min(self.dp[target], self.racecar(target - 2**(n - 1) + 2**m) + n + m + 1)
        return self.dp[target]
# leetcode submit region end(Prohibit modification and deletion)
