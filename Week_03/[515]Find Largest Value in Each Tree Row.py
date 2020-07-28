# You need to find the largest value in each row of a binary tree. 
# 
#  Example: 
#  
# Input: 
# 
#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 
# 
# Output: [1, 3, 9]
#  
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 81 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res, level = [], [root]
        while any(level):
            res.append(max(root.val for root in level))
            level = [kid for root in level for kid in (root.left, root.right) if kid]
        return res
# leetcode submit region end(Prohibit modification and deletion)
