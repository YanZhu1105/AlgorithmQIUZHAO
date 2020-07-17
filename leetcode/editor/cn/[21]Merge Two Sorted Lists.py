# Merge two sorted linked lists and return it as a new sorted list. The new list
#  should be made by splicing together the nodes of the first two lists. 
# 
#  Example: 
# 
#  
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#  
#  Related Topics 链表 
#  👍 1152 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists_recursion(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # 空间复杂度降为O(1)
    def mergeTwoLists_iteration(self, l1, l2):
        dummy = ListNode(None)
        pre = dummy

        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1, pre = l1.next, pre.next
            else:
                pre.next = l2
                l2, pre = l2.next, pre.next

        pre.next = l1 if l1 else l2
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
