# Invert a binary tree. 
# 
#  Example: 
# 
#  Input: 
# 
#  
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9 
# 
#  Output: 
# 
#  
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1 
# 
#  Trivia: 
# This problem was inspired by this original tweet by Max Howell: 
# 
#  Google: 90% of our engineers use the software you wrote (Homebrew), but you c
# an’t invert a binary tree on a whiteboard so f*** off. 
#  Related Topics 树 
#  👍 503 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return []
        if not root.left and not root.right: return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
# leetcode submit region end(Prohibit modification and deletion)
