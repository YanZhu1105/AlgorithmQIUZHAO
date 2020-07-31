# A gene string can be represented by an 8-character long string, with choices f
# rom "A", "C", "G", "T". 
# 
#  Suppose we need to investigate about a mutation (mutation from "start" to "en
# d"), where ONE mutation is defined as ONE single character changed in the gene s
# tring. 
# 
#  For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation. 
# 
#  Also, there is a given gene "bank", which records all the valid gene mutation
# s. A gene must be in the bank to make it a valid gene string. 
# 
#  Now, given 3 things - start, end, bank, your task is to determine what is the
#  minimum number of mutations needed to mutate from "start" to "end". If there is
#  no such a mutation, return -1. 
# 
#  Note: 
# 
#  
#  Starting point is assumed to be valid, so it might not be included in the ban
# k. 
#  If multiple mutations are needed, all mutations during in the sequence must b
# e valid. 
#  You may assume start and end string is not the same. 
#  
# 
#  
# 
#  Example 1: 
# 
#  
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
# 
# return: 1
#  
# 
#  
# 
#  Example 2: 
# 
#  
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# 
# return: 2
#  
# 
#  
# 
#  Example 3: 
# 
#  
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
# 
# return: 3
#  
# 
#  
#  👍 42 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if not start or end not in bank: return -1
        hashmap = {'A': 'CGT', 'C': 'AGT', 'G': 'ACT', 'T': 'ACG'}
        bank = set(bank)
        queue = collections.deque()
        queue.append((start, 0))

        while queue:
            curr, depth = queue.popleft()
            for i in range(len(curr)):
                for char in hashmap[curr[i]]:
                    next_ = curr[:i] + char + curr[i+1:]
                    if next_ == end: return depth + 1
                    if next_ in bank:
                        queue.append((next_, depth + 1))
                        bank.remove(next_)
        return -1

    # 双向BFS
    def minMutationDouble(self, start: str, end: str, bank: List[str]) -> int:
        def bfs(queue, visited, other_visited):
            curr, depth = queue.popleft()
            for i in range(len(curr)):
                for letter in hashmap[curr[i]]:
                    neighbor = curr[:i] + letter + curr[i+1:]
                    if neighbor in other_visited: return depth + other_visited[neighbor] + 1
                    if neighbor not in visited and neighbor in bank:
                        queue.append((neighbor, depth + 1))
                        visited[neighbor] = depth + 1

        if not start or not end or end not in bank: return -1
        hashmap = {'A': 'CGT', 'C': 'AGT', 'G': 'ACT', 'T': 'ACG'}
        bank = set(bank)
        queue_start, queue_end = collections.deque(), collections.deque()
        visited_start, visited_end = collections.defaultdict(int), collections.defaultdict(int)
        visited_start[start], visited_end[end] = 0, 0
        queue_start.append((start, 0))
        queue_end.append((end, 0))

        while queue_start and queue_end:
            ans = bfs(queue_start, visited_start, visited_end)
            if ans: return ans
            ans = bfs(queue_end, visited_end, visited_start)
            if ans: return ans
        return -1


# leetcode submit region end(Prohibit modification and deletion)

S = Solution()
S.minMutationDouble("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"])