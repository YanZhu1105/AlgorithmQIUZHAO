# Given a string containing digits from 2-9 inclusive, return all possible lette
# r combinations that the number could represent. 
# 
#  A mapping of digit to letters (just like on the telephone buttons) is given b
# elow. Note that 1 does not map to any letters. 
# 
#  
# 
#  Example: 
# 
#  
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#  
# 
#  Note: 
# 
#  Although the above answer is in lexicographical order, your answer could be i
# n any order you want. 
#  Related Topics 字符串 回溯算法 
#  👍 806 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        def helper(path, index):
            if len(path) == len(digits):
                res.append(path[:])
                return

            for letter in mapping[digits[index]]:
                helper(path + letter, index + 1)

        res = []
        helper('', 0)
        return res

    def letterCombinations_better(self, digits):
        dict = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs",
                '8': "tuv", '9': "wxyz"}
        res = [''] if digits else []
        for digit in digits:
            res = [prev + curr for prev in res for curr in dict[digit]]
        return res
# leetcode submit region end(Prohibit modification and deletion)
