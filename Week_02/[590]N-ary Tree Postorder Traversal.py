# Given an n-ary tree, return the postorder traversal of its nodes' values. 
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
# Output: [5,6,3,2,4,1]
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null
# ,12,null,13,null,null,14]
# Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
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
#  👍 85 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        res = []
        stack = []
        stack.append(root)

        while stack:
            root = stack.pop()
            res.append(root.val)
            stack.extend(root.children)

        #也可以写 res[::-1], 不过空间复杂度会多O(N)，reversed的话，空间复杂度是O(1)
        return reversed(res)
# leetcode submit region end(Prohibit modification and deletion)
