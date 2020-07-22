# Given a binary tree, find its minimum depth. 
# 
#  The minimum depth is the number of nodes along the shortest path from the roo
# t node down to the nearest leaf node. 
# 
#  Note: A leaf is a node with no children. 
# 
#  Example: 
# 
#  Given binary tree [3,9,20,null,null,15,7], 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  return its minimum depth = 2. 
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 296 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepthRecursion(self, root: TreeNode) -> int:
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        depth = min(left, right) if left and right else left or right
        return 1 + depth

    def minDepthBFS(self, root):
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            root, level = queue.popleft()
            if not root: continue
            if not root.left and not root.right:
                return level
            queue.append((root.left, level + 1))
            queue.append((root.right, level + 1))

# leetcode submit region end(Prohibit modification and deletion)
