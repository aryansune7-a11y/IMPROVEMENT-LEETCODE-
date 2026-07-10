from bisect import bisect_right

class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:

        arr = sorted((nums[i], i) for i in range(n))

        pos = [0] * n
        comp = [0] * n 

        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        cid = 0
        comp[0] = 0
        for i in range(1, n):
            if arr[i][0] - arr[i - 1][0] > maxDiff:
                cid += 1
            comp[i] = cid

        groups = [[] for _ in range(cid + 1)]
        for i in range(n):
            groups[comp[i]].append(i)

        data = {}

        for c, idxs in enumerate(groups):
            m = len(idxs)

            reach = [0] * m
            r = 0
            for l in range(m):
                while r + 1 < m and arr[idxs[r + 1]][0] - arr[idxs[l]][0] <= maxDiff:
                    r += 1
                reach[l] = r

            LOG = max(1, m.bit_length())
            jump = [reach]
            for _ in range(1, LOG):
                prev = jump[-1]
                cur = [0] * m
                for i in range(m):
                    cur[i] = prev[prev[i]]
                jump.append(cur)

            data[c] = (idxs[0], jump)

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            pu = pos[u]
            pv = pos[v]

            if comp[pu] != comp[pv]:
                ans.append(-1)
                continue

            if pu > pv:
                pu, pv = pv, pu

            start, jump = data[comp[pu]]
            l = pu - start
            r = pv - start

            if l == r:
                ans.append(0)
                continue

            steps = 0
            cur = l

            for k in range(len(jump) - 1, -1, -1):
                nxt = jump[k][cur]
                if nxt < r:
                    cur = nxt
                    steps += 1 << k

            ans.append(steps + 1)

        return ans