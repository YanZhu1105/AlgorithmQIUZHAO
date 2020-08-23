# Given a string s and a non-empty string p, find all the start indices of p's a
# nagrams in s. 
# 
#  Strings consists of lowercase English letters only and the length of both str
# ings s and p will not be larger than 20,100. 
# 
#  The order of output does not matter. 
# 
#  Example 1:
#  
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#  
#  
# 
#  Example 2:
#  
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#  
#  Related Topics 哈希表 
#  👍 352 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        left, right, valid, res = 0, 0, 0, []
        need = collections.Counter(p)
        window = dict.fromkeys(need.keys(), 0)
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]: valid += 1
            while valid == len(need):
                if right - left == len(p):
                    res.append(left)
                c = s[left]
                left += 1
                if c in need:
                    if window[c] == need[c]: valid -= 1
                    window[c] -= 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
