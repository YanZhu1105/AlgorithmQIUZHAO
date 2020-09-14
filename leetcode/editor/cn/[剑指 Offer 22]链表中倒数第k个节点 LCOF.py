# English description is not available for the problem. Please switch to Chinese
# . Related Topics 链表 双指针 
#  👍 81 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        slow = fast = head
        for _ in range(k):
            fast = fast.next
        while fast:
            slow, fast = slow.next, fast.next
        return slow
# leetcode submit region end(Prohibit modification and deletion)
