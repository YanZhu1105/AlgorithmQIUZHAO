# Given a string S and a string T, find the minimum window in S which will conta
# in all the characters in T in complexity O(n). 
# 
#  Example: 
# 
#  
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
#  
# 
#  Note: 
# 
#  
#  If there is no such window in S that covers all characters in T, return the e
# mpty string "". 
#  If there is such window, you are guaranteed that there will always be only on
# e unique minimum window in S. 
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 687 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        window = dict.fromkeys(need.keys(), 0)
        valid, L, R, ans = 0, 0, 0, (-1, len(s))
        while R < len(s):
            c = s[R]
            R += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:  valid += 1
            while valid == len(need):
                ans = (L, R) if R - L < ans[1] - ans[0] else ans
                c = s[L]
                L += 1
                if c in need:
                    if window[c] == need[c]:    valid -= 1
                    window[c] -= 1
        if ans[0] == -1: return ""
        return s[ans[0]:] if ans[1] == len(s) else s[ans[0]:ans[1]]
# leetcode submit region end(Prohibit modification and deletion)
S = Solution()
S.minWindow('ADOBECODEBANC', 'ABC')