# Given a binary tree, return the inorder traversal of its nodes' values. 
# 
#  Example: 
# 
#  
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 
# Output: [1,3,2] 
# 
#  Follow up: Recursive solution is trivial, could you do it iteratively? 
#  Related Topics 栈 树 哈希表 
#  👍 585 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversalRecursion(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root):
            if not root: return

            helper(root.left)
            res.append(root.val)
            helper(root.right)

        res = []
        helper(root)
        return res

    def inorderTraversalIteration(self, root):
        if not root: return []
        stack = []
        res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
# leetcode submit region end(Prohibit modification and deletion)
