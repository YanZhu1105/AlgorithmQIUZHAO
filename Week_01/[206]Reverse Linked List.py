# Reverse a singly linked list. 
# 
#  Example: 
# 
#  
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#  
# 
#  Follow up: 
# 
#  A linked list can be reversed either iteratively or recursively. Could you im
# plement both? 
#  Related Topics 链表 
#  👍 1091 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        curr = head
        while curr:
            nex = curr.next
            curr.next = pre
            pre, curr = curr, nex

        return pre
# leetcode submit region end(Prohibit modification and deletion)
