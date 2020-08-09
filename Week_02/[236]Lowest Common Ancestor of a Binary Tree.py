# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes 
# in the tree. 
# 
#  According to the definition of LCA on Wikipedia: “The lowest common ancestor 
# is defined between two nodes p and q as the lowest node in T that has both p and
#  q as descendants (where we allow a node to be a descendant of itself).” 
# 
#  Given the following binary tree: root = [3,5,1,6,2,0,8,null,null,7,4] 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant o
# f itself according to the LCA definition.
#  
# 
#  
# 
#  Note: 
# 
#  
#  All of the nodes' values will be unique. 
#  p and q are different and both values will exist in the binary tree. 
#  
#  Related Topics 树 
#  👍 667 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        if root == p or root == q: return root

        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)

        if not left and not right: return
        if not left: return right
        if not right: return left

        return root

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in [None, p, q]: return root
        left = self.lowestCommonAncestor1(root.left, p, q)
        right = self.lowestCommonAncestor1(root.right, p, q)
        return root if left and right else left or right

# leetcode submit region end(Prohibit modification and deletion)
