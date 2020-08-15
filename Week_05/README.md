如何选择heuristic: http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html
37: 用逻辑符号确实妙！用位运算来压缩状态。推而广之，只要是要开visitied，基本上可以用binary来压缩状态，加速也省空间
1091：visited 究竟是放在neighbor那里，还是pop那里，还是需要多思考。
heuristic基本上曼哈顿通用，max(abs(x - goal[x]) , abs(y - goal[y]))。8方向的话，diagonal可以用。

双向BFS写的很熟练了。位运算以前没有接触过，要多练，很好的trick，很多地方能用到。A star并不难。并查集很有趣，不难，就是
比较局限。

class TwoEndedBFS:    
    def ladderLengthDoubleEnded(self, beginWord, endWord, wordList):
        def bfs(queue, visited, other_visited):
            curr, depth = queue.popleft()
            for i in range(len(curr)):
                temp = curr[:i] + '*' + curr[i + 1:]
                for neighbor in all_combo[temp]:
                    if neighbor in other_visited: return depth + other_visited[neighbor]
                    if neighbor not in visited:
                        queue.append((neighbor, depth + 1))
                        visited[neighbor] = depth + 1
            return None

        if not beginWord or endWord not in wordList: return 0
        all_combo = collections.defaultdict(list)
        wordList = set(wordList)
        for word in wordList:
            for i in range(len(word)):
                all_combo[word[:i] + '*' + word[i + 1:]].append(word)

        queue_begin, queue_end = collections.deque(), collections.deque()
        visited_begin, visited_end = collections.defaultdict(int), collections.defaultdict(int)
        queue_begin.append((beginWord, 1))
        queue_end.append((endWord, 1))
        visited_begin[beginWord], visited_end[endWord] = 1, 1

        while queue_begin and queue_end:
            ans = bfs(queue_begin, visited_begin, visited_end)
            if ans: return ans
            ans = bfs(queue_end, visited_end, visited_begin)
            if ans: return ans
        return 0

    def ladderLengthSet(self, beginWord: str, endWord: str, wordList) -> int:
        if not beginWord or endWord not in wordList: return 0
        bq, eq, bv, ev, wordList = {(beginWord, 1)}, {(endWord, 1)}, {beginWord: 1}, {endWord: 1}, set(wordList)
        while bq:
            t = set()
            for word, step in bq:
                for neighbor in [word[:i] + letter + word[i+1:] for i in range(len(word)) for letter in 'qwertyuiopasdfghjklzxcvbnm']:
                    if neighbor in wordList:
                        if neighbor in ev: return step + ev[neighbor]
                        if neighbor not in bv:
                            t.add((neighbor, step + 1))
                            bv[neighbor] = step + 1
            bq = t
            if len(bq) > len(eq):
                bq, eq = eq, bq
                bv, ev = ev, bv
        return 0

    def ladderLengthSet2(self, beginWord: str, endWord: str, wordList) -> int:
        if not beginWord or endWord not in wordList: return 0
        ans = 2
        bq, eq, wordList = {beginWord}, {endWord}, set(wordList)
        wordList.discard(beginWord)
        while bq:
            neighbor = set([word[:i] + char + word[i + 1:] for word in bq for i in range(len(word)) for char in
                            'qwertyuiopasdfghjklzxcvbnm'])
            bq = neighbor & wordList
            if bq & eq: return ans
            ans += 1
            if len(bq) > len(eq):
                bq, eq = eq, bq
            wordList -= bq
        return 0