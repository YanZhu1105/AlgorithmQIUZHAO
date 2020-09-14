# Given a string s, find the length of the longest substring without repeating c
# haracters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a 
# substring.
#  
# 
#  Example 4: 
# 
#  
# Input: s = ""
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 5 * 104 
#  s consists of English letters, digits, symbols and spaces. 
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 4304 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        res, left, right, window = 1, 0, 0, collections.defaultdict(int)
        while right < len(s):
            r = s[right]
            right += 1
            window[r] += 1
            while window[r] > 1:
                l = s[left]
                left += 1
                window[l] -= 1
            res = max(res, right - left)
        return res
# leetcode submit region end(Prohibit modification and deletion)
