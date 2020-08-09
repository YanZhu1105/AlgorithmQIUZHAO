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
#  👍 391 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    # 单向BFS，基础
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not beginWord or endWord not in wordList: return 0
        all_combo = collections.defaultdict(list)
        queue, wordList = collections.deque(), set(wordList)

        for word in wordList:
            for i in range(len(word)):
                all_combo[word[:i] + '*' + word[i + 1:]].append(word)

        queue.append((beginWord, 1))
        while queue:
            curr, depth = queue.popleft()
            for i in range(len(curr)):
                temp = curr[:i] + '*' + curr[i + 1:]
                for neighbor in all_combo[temp]:
                    if neighbor == endWord: return depth + 1
                    if neighbor in wordList:
                        queue.append((neighbor, depth + 1))
                        wordList.remove(neighbor)
        return 0

    # 双向BFS
    def ladderLengthDoubleEnded(self, beginWord, endWord, wordList):
        def bfs(queue, visited, other_visited):
            curr, depth = queue.popleft()
            for i in range(len(curr)):
                temp = curr[:i] + '*' + curr[i + 1:]
                for neighbor in all_combo[temp]:
                    if neighbor in other_visited: return depth + other_visited[neighbor]
                    if neighbor not in visited:
                        queue.append((neighbor, depth + 1))
                        visited[neighbor] = depth + 1
            return None

        if not beginWord or endWord not in wordList: return 0
        all_combo = collections.defaultdict(list)
        wordList = set(wordList)
        for word in wordList:
            for i in range(len(word)):
                all_combo[word[:i] + '*' + word[i + 1:]].append(word)

        queue_begin, queue_end = collections.deque(), collections.deque()
        visited_begin, visited_end = collections.defaultdict(int), collections.defaultdict(int)
        queue_begin.append((beginWord, 1))
        queue_end.append((endWord, 1))
        visited_begin[beginWord], visited_end[endWord] = 1, 1

        while queue_begin and queue_end:
            ans = bfs(queue_begin, visited_begin, visited_end)
            if ans: return ans
            ans = bfs(queue_end, visited_end, visited_begin)
            if ans: return ans
        return 0

    def ladderLengthSet(self, beginWord: str, endWord: str, wordList) -> int:
        if not beginWord or endWord not in wordList: return 0
        bq, eq, bv, ev, wordList = {(beginWord, 1)}, {(endWord, 1)}, {beginWord: 1}, {endWord: 1}, set(wordList)
        while bq:
            t = set()
            for word, step in bq:
                for neighbor in [word[:i] + letter + word[i+1:] for i in range(len(word)) for letter in 'qwertyuiopasdfghjklzxcvbnm']:
                    if neighbor in wordList:
                        if neighbor in ev: return step + ev[neighbor]
                        if neighbor not in bv:
                            t.add((neighbor, step + 1))
                            bv[neighbor] = step + 1
            bq = t
            if len(bq) > len(eq):
                bq, eq = eq, bq
                bv, ev = ev, bv
        return 0

    def ladderLengthSet2(self, beginWord: str, endWord: str, wordList) -> int:
        if not beginWord or endWord not in wordList: return 0
        ans = 2
        bq, eq, wordList = {beginWord}, {endWord}, set(wordList)
        wordList.discard(beginWord)
        while bq:
            neighbor = set([word[:i] + char + word[i + 1:] for word in bq for i in range(len(word)) for char in
                            'qwertyuiopasdfghjklzxcvbnm'])
            bq = neighbor & wordList
            if bq & eq: return ans
            ans += 1
            if len(bq) > len(eq):
                bq, eq = eq, bq
            wordList -= bq
        return 0
# leetcode submit region end(Prohibit modification and deletion)

S = Solution()
print(S.ladderLengthSet2("hot",
"dog",
["hot","dog"]))
