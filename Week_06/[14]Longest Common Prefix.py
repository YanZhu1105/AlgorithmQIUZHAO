# Write a function to find the longest common prefix string amongst an array of 
# strings. 
# 
#  If there is no common prefix, return an empty string "". 
# 
#  Example 1: 
# 
#  
# Input: ["flower","flow","flight"]
# Output: "fl"
#  
# 
#  Example 2: 
# 
#  
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#  
# 
#  Note: 
# 
#  All given inputs are in lowercase letters a-z. 
#  Related Topics 字符串 
#  👍 1229 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 纵向扫描
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        for i in range(len(strs[0])):
            char = strs[0][i]
            # for j in range(1, len(strs)):
            #     if i == len(strs[j]) or strs[j][i] != char: return strs[0][:i]
            if any(i == len(strs[j]) or strs[j][i] != char for j in range(1, len(strs))):
                return strs[0][:i]
        return strs[0]

    # Trie
    def longestCommonPrefixTrie(self, strs):
        if not strs: return ''
        trie = collections.defaultdict(dict)
        node = trie
        for char in strs[0]:
            node = node.setdefault(char, {})
        node['#'] = True

        count = len(strs[0])
        for word in strs[1:]:
            node, temp = trie, 0
            for char in word:
                if char in node: node = node[char]
                else: break
                temp += 1
            count = min(count, temp)
            if count == 0: break
        return strs[0][:count]

    # zip
    # zip完后，就纵向对齐了，比如["flower","flow","flight"] -> [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
    def longestCommonPrefixZip(self, strs):
        """
        :type strs: List[str]; rtype: str
        """
        sz, ret = zip(*strs), ""
        # looping corrected based on @StefanPochmann's comment below
        for c in sz:
            if len(set(c)) > 1: break
            ret += c[0]
        return ret

    # max, min 更绝
    # call min/max 会alphabetical sort strs, min给第一个，max给最后一个，直接比较这两个最不同的就ok
    class Solution:
        def longestCommonPrefixMax(self, S: List[str]) -> str:
            if not S: return ''
            m, M, i = min(S), max(S), 0
            for i, char in enumerate(m):
                if char != M[i]: break
            return m[:i]
# leetcode submit region end(Prohibit modification and deletion)
