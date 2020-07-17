# Given an array of strings, group anagrams together. 
# 
#  Example: 
# 
#  
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ] 
# 
#  Note: 
# 
#  
#  All inputs will be in lowercase. 
#  The order of your output does not matter. 
#  
#  Related Topics 哈希表 字符串 
#  👍 393 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def groupAnagrams_strAsKey(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = collections.defaultdict(list)

        for str in strs:
            hashmap[tuple(sorted(str))].append(str)

        return hashmap.values()


    # 空间换时间，每次key不用sort，直接开一个size 26的counter, 优点在于单词长的话，O(1)比sort的O(LogK)快，缺点在于不支持unicode，通用性较差
    def groupAnagrams_ASCIIasKey(self, strs):
        hashmap = collections.defaultdict(list)

        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord('a')] += 1
            hashmap[tuple(count)].append(str)

        return list(hashmap.values())
# leetcode submit region end(Prohibit modification and deletion)
