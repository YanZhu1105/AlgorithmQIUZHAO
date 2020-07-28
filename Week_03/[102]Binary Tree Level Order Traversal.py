# Given a binary tree, return the level order traversal of its nodes' values. (i
# e, from left to right, level by level). 
# 
#  
# For example: 
# Given binary tree [3,9,20,null,null,15,7], 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
#  
#  
# return its level order traversal as: 
#  
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 
#  👍 574 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)

        while queue:
            level = []
            for _ in range(len(queue)):
                root = queue.popleft()
                level.append(root.val)
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)
            res.append(level)
        return res

    # list comprehension
    def levelOrderListComprehension(self, root):
        res, level = [], [root]
        while root and level:
            res.append([root.val for root in level])
            level = [kid for root in level for kid in (root.left, root.right) if kid]
        return res

# leetcode submit region end(Prohibit modification and deletion)
