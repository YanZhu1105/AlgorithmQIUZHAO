# Given two words (beginWord and endWord), and a dictionary's word list, find th
# e length of shortest transformation sequence from beginWord to endWord, such tha
# t: 
# 
#  
#  Only one letter can be changed at a time. 
#  Each transformed word must exist in the word list. 
#  
# 
#  Note: 
# 
#  
#  Return 0 if there is no such transformation sequence. 
#  All words have the same length. 
#  All words contain only lowercase alphabetic characters. 
#  You may assume no duplicates in the word list. 
#  You may assume beginWord and endWord are non-empty and are not the same. 
#  
# 
#  Example 1: 
# 
#  
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output: 5
# 
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog
# " -> "cog",
# return its length 5.
#  
# 
#  Example 2: 
# 
#  
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: 0
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible trans
# formation.
#  
# 
#  
#  
#  Related Topics 广度优先搜索 
#  👍 592 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if not beginWord or endWord not in wordList: return 0
        bq, eq, bv, ev = {(beginWord, 1)}, {(endWord, 1)}, {beginWord: 1}, {endWord: 1}
        while bq:
            temp = set()
            for word, step in bq:
                for neigbhor in [word[:i] + char + word[i+1:] for i in range(len(word)) for char in 'qwertyuiopasdfghjklzxcvbnm']:
                    if neigbhor in wordList and neigbhor not in bv:
                        if neigbhor in ev:
                            return ev[neigbhor] + step
                        temp.add((neigbhor, step + 1))
                        bv[neigbhor] = step + 1
            bq = temp
            if len(bq) > len(eq):
                bq, eq, bv, ev = eq, bq, ev, bv
        return 0
# leetcode submit region end(Prohibit modification and deletion)
