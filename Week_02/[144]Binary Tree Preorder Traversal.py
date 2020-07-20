# Given a binary tree, return the preorder traversal of its nodes' values. 
# 
#  Example: 
# 
#  
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 
# Output: [1,2,3]
#  
# 
#  Follow up: Recursive solution is trivial, could you do it iteratively? 
#  Related Topics 栈 树 
#  👍 313 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversalRecursion(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def helper(root):
            if not root: return

            res.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        return res

    # 本质上迭代和递归是一回事，迭代就是手动维护一个stack罢了，逻辑不变
    def preorderTraversalIteration(self, root):
        if not root: return []
        res, stack = [], [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return res
# leetcode submit region end(Prohibit modification and deletion)
