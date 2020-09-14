# Sort a linked list in O(n log n) time using constant space complexity. 
# 
#  Example 1: 
# 
#  
# Input: 4->2->1->3
# Output: 1->2->3->4
#  
# 
#  Example 2: 
# 
#  
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5 
#  Related Topics 排序 链表 
#  👍 732 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortListRecursion(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid, slow.next = slow, None
        left, right = self.sortList(head), self.sortList(mid)
        head = dummy = ListNode(None)
        while left and right:
            if left.val < right.val:
                head.next, left = left, left.next
            else:
                head.next, right = right, right.next
            head = head.next
        head.next = left if left else right
        return dummy.next

    def sortListMerge(self, head):
        h, length, intv = head, 0, 1
        while h: h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        # merge the list in different intv.
        while intv < length:
            pre, h = res, res.next
            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, intv
                while i and h: h, i = h.next, i - 1
                if i: break  # no need to merge because the `h2` is None.
                h2, i = h, intv
                while i and h: h, i = h.next, i - 1
                c1, c2 = intv, intv - i  # the `c2`: length of `h2` can be small than the `intv`.
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            intv *= 2
        return res.next

# leetcode submit region end(Prohibit modification and deletion)
