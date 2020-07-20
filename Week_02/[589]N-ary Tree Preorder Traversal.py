# Given an n-ary tree, return the preorder traversal of its nodes' values. 
# 
#  Nary-Tree input serialization is represented in their level order traversal, 
# each group of children is separated by the null value (See examples). 
# 
#  
# 
#  Follow up: 
# 
#  Recursive solution is trivial, could you do it iteratively? 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,3,5,6,2,4]
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null
# ,12,null,13,null,null,14]
# Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
#  
# 
#  
#  Constraints: 
# 
#  
#  The height of the n-ary tree is less than or equal to 1000 
#  The total number of nodes is between [0, 10^4] 
#  
#  Related Topics 树 
#  👍 89 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        stack = [root]
        res = []

        while stack:
            root = stack.pop()
            res.append(root.val)
            stack.extend(reversed(root.children))
        return res

    def preorderRecursion(self, root):
        def helper(root):
            if not root: return

            res.append(root.val)

            for child in root.children:
                helper(child)

            return res

        res = []
        helper(root)
        return res
# leetcode submit region end(Prohibit modification and deletion)
