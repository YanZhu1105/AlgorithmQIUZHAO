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
        if not start or end not in bank: return -1
        hashmap = {'A': 'CGT', 'C': 'AGT', 'G': 'ACT', 'T': 'ACG'}
        bq, eq, bv, ev = {(start, 0)}, {(end, 0)}, {start: 0}, {end: 0}
        bank = set(bank)
        while bq:
            temp = set()
            for curr, step in bq:
                for neighbor in [curr[:i] + letter + curr[i+1:] for i in range(len(curr)) for letter in hashmap[curr[i]]]:
                    if neighbor in bank:
                        if neighbor in ev: return step + ev[neighbor] + 1
                        if neighbor not in bv:
                            temp.add((neighbor, step + 1))
                            bv[neighbor] = step + 1
            bq = temp
            if len(bq) > len(eq):
                bq, eq = eq, bq
                bv, ev = ev, bv
        return -1
# leetcode submit region end(Prohibit modification and deletion)

S = Solution()
S.minMutation("AAAACCCC",
"CCCCCCCC",
["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"])