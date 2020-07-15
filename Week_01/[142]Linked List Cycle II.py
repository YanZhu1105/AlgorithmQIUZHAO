# Given a linked list, return the node where the cycle begins. If there is no cy
# cle, return null. 
# 
#  To represent a cycle in the given linked list, we use an integer pos which re
# presents the position (0-indexed) in the linked list where tail connects to. If 
# pos is -1, then there is no cycle in the linked list. 
# 
#  Note: Do not modify the linked list. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the s
# econd node.
#  
# 
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the f
# irst node.
#  
# 
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
#  
# 
#  
# 
#  
# 
#  Follow-up: 
# Can you solve it without using extra space? 
#  Related Topics 链表 双指针 
#  👍 535 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head

        while True:
            if not fast or not fast.next: return None
            slow = slow.next
            fast = fast.next.next
            if fast == slow: break

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
# leetcode submit region end(Prohibit modification and deletion)
