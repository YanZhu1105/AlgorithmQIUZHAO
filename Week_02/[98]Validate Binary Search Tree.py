# Given a binary tree, determine if it is a valid binary search tree (BST). 
# 
#  Assume a BST is defined as follows: 
# 
#  
#  The left subtree of a node contains only nodes with keys less than the node's
#  key. 
#  The right subtree of a node contains only nodes with keys greater than the no
# de's key. 
#  Both the left and right subtrees must also be binary search trees. 
#  
# 
#  
# 
#  Example 1: 
# 
#  
#     2
#    / \
#   1   3
# 
# Input: [2,1,3]
# Output: true
#  
# 
#  Example 2: 
# 
#  
#     5
#    / \
#   1   4
#      / \
#     3   6
# 
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#  
#  Related Topics 树 深度优先搜索 
#  👍 672 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBSTRecursion(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root, lower = float('-inf'), upper = float('inf')):
            if not root: return True
            if root.val <= lower or root.val >= upper: return False

            return helper(root.left, lower, root.val) and helper(root.right, root.val, upper)

        return helper(root)

    # 二叉搜索树 == 中序遍历为升序
    def isValidBSTInorder(self, root):
        if not root: return True
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True

# leetcode submit region end(Prohibit modification and deletion)
