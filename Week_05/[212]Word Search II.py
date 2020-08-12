# Given a 2D board and a list of words from the dictionary, find all words in th
# e board. 
# 
#  Each word must be constructed from letters of sequentially adjacent cell, whe
# re "adjacent" cells are those horizontally or vertically neighboring. The same l
# etter cell may not be used more than once in a word. 
# 
#  
# 
#  Example: 
# 
#  
# Input: 
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
# 
# Output: ["eat","oath"]
#  
# 
#  
# 
#  Note: 
# 
#  
#  All inputs are consist of lowercase letters a-z. 
#  The values of words are distinct. 
#  
#  Related Topics 字典树 回溯算法 
#  👍 210 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
directions = {(-1, 0), (1, 0), (0, 1), (0, -1)}
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not words: return []
        self.board = board
        self.m, self.n, self.res, self.words = len(board), len(board[0]), set(), set(words)
        self.buildTrie()
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in self.trie:
                    self.dfs(board[i][j], i, j, self.trie[board[i][j]])
        return list(self.res)

    def buildTrie(self):
        self.trie, end_of_word = {}, '#'
        for word in self.words:
            root = self.trie
            for char in word:
                root = root.setdefault(char, {})
            root['#'] = True

    def dfs(self, path, x, y, root):
        if '#' in root:
            self.res.add(path[:])           # 这里不能return，注意细节

        temp, self.board[x][y] = self.board[x][y], '@'
        for new_x, new_y in [(x + dx, y + dy) for dx, dy in directions]:
            if 0 <= new_x < self.m and 0 <= new_y < self.n and self.board[new_x][new_y] in root:
                self.dfs(path + self.board[new_x][new_y], new_x, new_y, root[self.board[new_x][new_y]])
        self.board[x][y] = temp

    # better version
    def findWords2(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}  # 构造字典树
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True

        def search(i, j, node, pre, visited):  # (i,j)当前坐标，node当前trie树结点，pre前面的字符串，visited已访问坐标
            if '#' in node:  # 已有字典树结束
                res.add(pre)  # 添加答案
            for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                _i, _j = i + di, j + dj
                if -1 < _i < h and -1 < _j < w and board[_i][_j] in node and (_i, _j) not in visited:  # 可继续搜索
                    search(_i, _j, node[board[_i][_j]], pre + board[_i][_j], visited | {(_i, _j)})  # dfs搜索

        res, h, w = set(), len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if board[i][j] in trie:  # 可继续搜索
                    search(i, j, trie[board[i][j]], board[i][j], {(i, j)})  # dfs搜索
        return list(res)
