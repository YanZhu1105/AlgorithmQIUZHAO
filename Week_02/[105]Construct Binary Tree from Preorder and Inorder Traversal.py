# Given preorder and inorder traversal of a tree, construct the binary tree. 
# 
#  Note: 
# You may assume that duplicates do not exist in the tree. 
# 
#  For example, given 
# 
#  
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7] 
# 
#  Return the following binary tree: 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7 
#  Related Topics 树 深度优先搜索 数组 
#  👍 579 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return
            root = TreeNode(preorder[preorder_left])
            size_of_left = index[root.val] - inorder_left
            root.left = helper(preorder_left + 1, preorder_left + size_of_left, inorder_left, index[root.val] - 1)
            root.right = helper(preorder_left + size_of_left + 1, preorder_right, index[root.val] + 1, inorder_right)

            return root

        index = {element: i for i, element in enumerate(inorder)}
        n = len(inorder) - 1
        return helper(0, n, 0, n)

    # 这种对递归的理解真的是厉害，完全就是只考虑终止条件，process和子问题。化繁为简！
    # 虽然这个solution慢，因为有数组的添加删除。
    def buildTreeBetter(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0: ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root
# leetcode submit region end(Prohibit modification and deletion)
