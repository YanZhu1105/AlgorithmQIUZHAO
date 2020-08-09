class Solution:
    def generateParenthesis(self, n: int):
        res, queue = [], collections.deque()
        queue.append(('', n, n))
        while queue:
            path, left, right = queue.popleft()
            if left == right == 0:
                res.append(path[:])
                continue
            if left > 0: queue.append((path + '(', left - 1, right))
            if right > left: queue.append((path + ')', left, right - 1))
        return res

    1
    2
    5
    14
    42
    132
    429
    1430