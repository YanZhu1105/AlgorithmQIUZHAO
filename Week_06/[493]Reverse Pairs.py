# Given an array nums, we call (i, j) an important reverse pair if i < j and num
# s[i] > 2*nums[j]. 
# 
#  You need to return the number of important reverse pairs in the given array. 
# 
# 
#  Example1:
#  
# Input: [1,3,2,3,1]
# Output: 2
#  
# 
#  Example2:
#  
# Input: [2,4,3,5,1]
# Output: 3
#  
# 
#  Note: 
#  
#  The length of the given array will not exceed 50,000. 
#  All the numbers in the input array are in the range of 32-bit integer. 
#  
#  Related Topics 排序 树状数组 线段树 二分查找 分治算法 
#  👍 123 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def mergeSort(nums, begin, end):
            if begin >= end: return 0
            mid = (begin + end) >> 1
            count = mergeSort(nums, begin, mid) + mergeSort(nums, mid + 1, end)
            t, i, temp = begin, begin, []
            for j in range(mid + 1, end + 1):
                while t <= mid and nums[t] <= 2 * nums[j]:
                    t += 1
                while i <= mid and nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                temp.append(nums[j])
                count += mid - t + 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            nums[begin: end + 1] = temp
            return count
        return mergeSort(nums, 0, len(nums)-1)
# leetcode submit region end(Prohibit modification and deletion)
S = Solution()
S.reversePairs([1,3,2,3,1])