# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all ele
# ments in arr2 are also in arr1. 
# 
#  Sort the elements of arr1 such that the relative ordering of items in arr1 ar
# e the same as in arr2. Elements that don't appear in arr2 should be placed at th
# e end of arr1 in ascending order. 
# 
#  
#  Example 1: 
#  Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
#  
#  
#  Constraints: 
# 
#  
#  arr1.length, arr2.length <= 1000 
#  0 <= arr1[i], arr2[i] <= 1000 
#  Each arr2[i] is distinct. 
#  Each arr2[i] is in arr1. 
#  
#  Related Topics 排序 数组 
#  👍 76 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count, mark = collections.Counter(arr1), 0
        for num in arr2:
            if num in count:
                for i in range(count[num]):
                    arr1[mark] = num
                    mark += 1
                del count[num]
        arr1[mark:] = sorted(list(count.elements()))
        return arr1
# leetcode submit region end(Prohibit modification and deletion)
