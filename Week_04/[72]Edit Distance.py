# Given two words word1 and word2, find the minimum number of operations require
# d to convert word1 to word2. 
# 
#  You have the following 3 operations permitted on a word: 
# 
#  
#  Insert a character 
#  Delete a character 
#  Replace a character 
#  
# 
#  Example 1: 
# 
#  
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#  
# 
#  Example 2: 
# 
#  
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#  
#  Related Topics 字符串 动态规划 
#  👍 1031 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[float('inf') for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        for row in range(len(dp)):
            dp[row][0] = row
        for col in range(len(dp[0])):
            dp[0][col] = col
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                dp[row][col] = min(dp[row-1][col] + 1, dp[row][col-1] + 1, dp[row-1][col-1] + (word1[row-1] != word2[col-1]))
        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
