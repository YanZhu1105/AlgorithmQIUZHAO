# Alice and Bob take turns playing a game, with Alice starting first. 
# 
#  Initially, there is a number N on the chalkboard. On each player's turn, that
#  player makes a move consisting of: 
# 
#  
#  Choosing any x with 0 < x < N and N % x == 0. 
#  Replacing the number N on the chalkboard with N - x. 
#  
# 
#  Also, if a player cannot make a move, they lose the game. 
# 
#  Return True if and only if Alice wins the game, assuming both players play op
# timally. 
# 
#  
# 
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.
#  
# 
#  
#  Example 2: 
# 
#  
# Input: 3
# Output: false
# Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= N <= 1000 
#  
#  
#  Related Topics 数学 动态规划 
#  👍 165 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 直接 return N % 2 == 0 也行，练一下dp吧
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        dp = [False for _ in range(N + 1)]
        dp[2] = True

        for i in range(3, N + 1):
            for j in range(1, i//2):
                if i % j == 0 and not dp[i - j]:
                    dp[i] = True
                    break
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
