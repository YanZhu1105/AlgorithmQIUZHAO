# Given a non negative integer number num. For every numbers i in the range 0 ≤ 
# i ≤ num calculate the number of 1's in their binary representation and return th
# em as an array. 
# 
#  Example 1: 
# 
#  
# Input: 2
# Output: [0,1,1] 
# 
#  Example 2: 
# 
#  
# Input: 5
# Output: [0,1,1,2,1,2]
#  
# 
#  Follow up: 
# 
#  
#  It is very easy to come up with a solution with run time O(n*sizeof(integer))
# . But can you do it in linear time O(n) /possibly in a single pass? 
#  Space complexity should be O(n). 
#  Can you do it like a boss? Do it without using any builtin function like __bu
# iltin_popcount in c++ or in any other language. 
#  Related Topics 位运算 动态规划 
#  👍 373 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0, 1, 1]
        for i in range(3, num + 1):
            res.append(res[i & i-1] + 1)            # 打掉最低位的1，加 1
        return res[:num + 1]
# leetcode submit region end(Prohibit modification and deletion)