# 
# There are N students in a class. Some of them are friends, while some are not.
#  Their friendship is transitive in nature. For example, if A is a direct friend 
# of B, and B is a direct friend of C, then A is an indirect friend of C. And we d
# efined a friend circle is a group of students who are direct or indirect friends
# .
#  
# 
#  
# Given a N*N matrix M representing the friend relationship between students in 
# the class. If M[i][j] = 1, then the ith and jth students are direct friends with
#  each other, otherwise not. And you have to output the total number of friend ci
# rcles among all the students.
#  
# 
#  Example 1: 
#  
# Input: 
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a frie
# nd circle. The 2nd student himself is in a friend circle. So return 2.
#  
#  
# 
#  Example 2: 
#  
# Input: 
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd stude
# nts are direct friends, so the 0th and 2nd students are indirect friends. All of
#  them are in the same friend circle, so return 1.
#  
#  
# 
# 
#  Note: 
#  
#  N is in range [1,200]. 
#  M[i][i] = 1 for all students. 
#  If M[i][j] = 1, then M[j][i] = 1. 
#  
#  Related Topics 深度优先搜索 并查集 
#  👍 289 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M: return 0
        n = len(M)
        parent = [i for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1: self._union(parent, i, j)
        return len(set([self._parent(parent, i) for i in range(n)]))

    def _union(self, parent, i, j):
        p1 = self._parent(parent, i)
        p2 = self._parent(parent, j)
        parent[p2] = p1

    def _parent(self, parent, i):
        root = i
        while parent[root] != root:
            root = parent[root]
        while parent[i] != i:
            parent[i], i = root, parent[i]
        return root
# leetcode submit region end(Prohibit modification and deletion)
