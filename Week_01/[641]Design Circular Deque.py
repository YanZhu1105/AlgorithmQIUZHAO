# Design your implementation of the circular double-ended queue (deque). 
# 
#  Your implementation should support following operations: 
# 
#  
#  MyCircularDeque(k): Constructor, set the size of the deque to be k. 
#  insertFront(): Adds an item at the front of Deque. Return true if the operati
# on is successful. 
#  insertLast(): Adds an item at the rear of Deque. Return true if the operation
#  is successful. 
#  deleteFront(): Deletes an item from the front of Deque. Return true if the op
# eration is successful. 
#  deleteLast(): Deletes an item from the rear of Deque. Return true if the oper
# ation is successful. 
#  getFront(): Gets the front item from the Deque. If the deque is empty, return
#  -1. 
#  getRear(): Gets the last item from Deque. If the deque is empty, return -1. 
#  isEmpty(): Checks whether Deque is empty or not. 
#  isFull(): Checks whether Deque is full or not. 
#  
# 
#  
# 
#  Example: 
# 
#  
# MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 
# 3
# circularDeque.insertLast(1);			// return true
# circularDeque.insertLast(2);			// return true
# circularDeque.insertFront(3);			// return true
# circularDeque.insertFront(4);			// return false, the queue is full
# circularDeque.getRear();  			// return 2
# circularDeque.isFull();				// return true
# circularDeque.deleteLast();			// return true
# circularDeque.insertFront(4);			// return true
# circularDeque.getFront();			// return 4
#  
# 
#  
# 
#  Note: 
# 
#  
#  All values will be in the range of [0, 1000]. 
#  The number of operations will be in the range of [1, 1000]. 
#  Please do not use the built-in Deque library. 
#  
#  Related Topics 设计 队列 
#  👍 46 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.deque = []
        self.size = k
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.deque) < self.size:
            self.deque.insert(0, value)
            return True
        else:
            return False
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.deque) < self.size:
            self.deque.append(value)
            return True
        else:
            return False

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.deque:
            self.deque.pop(0)
            return True
        else:
            return False
        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.deque:
            self.deque.pop()
            return True
        else:
            return False
        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.deque:
            return self.deque[0]
        else:
            return -1
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.deque:
            return self.deque[-1]
        else:
            return -1

        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return False if self.deque else True

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return True if len(self.deque) == self.size else False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# leetcode submit region end(Prohibit modification and deletion)
