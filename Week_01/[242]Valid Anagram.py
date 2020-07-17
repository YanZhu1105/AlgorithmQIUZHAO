# Given two strings s and t , write a function to determine if t is an anagram o
# f s. 
# 
#  Example 1: 
# 
#  
# Input: s = "anagram", t = "nagaram"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s = "rat", t = "car"
# Output: false
#  
# 
#  Note: 
# You may assume the string contains only lowercase alphabets. 
# 
#  Follow up: 
# What if the inputs contain unicode characters? How would you adapt your soluti
# on to such case? 
#  Related Topics 排序 哈希表 
#  👍 217 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = collections.defaultdict(int)

        for char in s: hashmap[char] += 1

        for char in t: hashmap[char] -= 1

        return all(count == 0 for count in hashmap.values())  # all函数的运用使得code很简洁，值得学习

# leetcode submit region end(Prohibit modification and deletion)
