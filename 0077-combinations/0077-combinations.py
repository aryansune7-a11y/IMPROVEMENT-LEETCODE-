class Solution:
    def combine(self, n: int, k: int):
        res = []
        comb = []

        def backtrack(start):
            if len(comb) == k:
                res.append(comb[:])
                return

            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1)
                comb.pop()

        backtrack(1)
        return res