# Given two words (beginWord and endWord), and a dictionary's word list, find al
# l shortest transformation sequence(s) from beginWord to endWord, such that: 
# 
#  
#  Only one letter can be changed at a time 
#  Each transformed word must exist in the word list. Note that beginWord is not
#  a transformed word. 
#  
# 
#  Note: 
# 
#  
#  Return an empty list if there is no such transformation sequence. 
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
# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
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
# Output: []
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible trans
# formation.
#  
# 
#  
#  
#  Related Topics 广度优先搜索 数组 字符串 回溯算法 
#  👍 299 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList: return []
        found, bq, eq, nq, rev = False, {beginWord}, {endWord}, set(), False
        while bq and not found:
            words -= set(bq)
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                    if y in words:
                        if y in eq:
                            found = True
                        else:
                            nq.add(y)
                        tree[y].add(x) if rev else tree[x].add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq, rev = eq, bq, not rev

        def bt(x):
            # return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
            if x == endWord: return [[x]]
            temp = []
            for y in tree[x]:
                for rest in bt(y):
                    temp.append([x] + rest)
            return temp
        return bt(beginWord)
# leetcode submit region end(Prohibit modification and deletion)
S = Solution()
S.findLadders(beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"])
