# Given an array of integers A sorted in non-decreasing order, return an array o
# f the squares of each number, also in sorted non-decreasing order. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 10000 
#  -10000 <= A[i] <= 10000 
#  A is sorted in non-decreasing order. 
#  
#  
#  Related Topics 数组 双指针 
#  👍 119 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A) - 1
        res = []
        while i <= j:
            if A[i] >= 0 or A[i]**2 < A[j]**2:
                res.append(A[j]**2)
                j -= 1
            else:
                res.append(A[i]**2)
                i += 1
        return reversed(res)

    def sortedSquaresShort(self, A):
        l, r, answer = 0, len(A) - 1, [0] * len(A)
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            answer[r - l] = max(left, right) ** 2
            l, r = l + (left > right), r - (left <= right)
        return answer
# leetcode submit region end(Prohibit modification and deletion)
