# Given a string, find the first non-repeating character in it and return its in
# dex. If it doesn't exist, return -1. 
# 
#  Examples: 
# 
#  
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode"
# return 2.
#  
# 
#  
# 
#  Note: You may assume the string contains only lowercase English letters. 
#  Related Topics 哈希表 字符串 
#  👍 254 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1
# leetcode submit region end(Prohibit modification and deletion)
