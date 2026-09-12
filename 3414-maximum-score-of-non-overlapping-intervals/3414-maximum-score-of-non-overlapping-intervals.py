from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:


        n = len(intervals)

        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        arr.sort()

        starts = [x[0] for x in arr]

        nxt = [0] * n

        for i in range(n):
            r = arr[i][1]
            nxt[i] = bisect_right(starts, r)

        memo = {}

        def better(a, b):

            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            return a if a[1] < b[1] else b

        def dp(i, k):
            if i == n or k == 0:
                return (0, [])

            if (i, k) in memo:
                return memo[(i, k)]

            skip = dp(i + 1, k)

            score, indices = dp(nxt[i], k - 1)

            take = (
                score + arr[i][2],
                sorted(indices + [arr[i][3]])
            )

            ans = better(skip, take)

            memo[(i, k)] = ans
            return ans

        return dp(0, 4)[1]