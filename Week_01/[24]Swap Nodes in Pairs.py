# Given a linked list, swap every two adjacent nodes and return its head. 
# 
#  You may not modify the values in the list's nodes, only nodes itself may be c
# hanged. 
# 
#  
# 
#  Example: 
# 
#  
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#  
#  Related Topics 链表 
#  👍 546 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Iteration
    def swapPairs_iteration(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head

        dummy = ListNode(None)
        dummy.next = head
        pre, curr = dummy, head

        while curr and curr.next:
            nex = curr.next
            pre.next, curr.next, nex.next = nex, nex.next, curr
            pre = curr
            curr = pre.next
        return dummy.next
    # Recursion

    def swapPairs_recursion(self, head):
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs_recursion(tmp.next)
            tmp.next = head
            return tmp
        return head


# leetcode submit region end(Prohibit modification and deletion)
