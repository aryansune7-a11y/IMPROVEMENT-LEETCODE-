
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        total = [0] * (4 * n)
        square = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, l, r, val):
            length = r - l + 1

            square[node] = (
                square[node]
                + 2 * val * total[node]
                + val * val * length
            ) % MOD

            total[node] = (total[node] + val * length) % MOD
            lazy[node] += val

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return

            mid = (l + r) // 2
            val = lazy[node]

            apply(node * 2, l, mid, val)
            apply(node * 2 + 1, mid + 1, r, val)

            lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(node, l, r, 1)
                return

            push(node, l, r)
            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr)

            total[node] = (
                total[node * 2] + total[node * 2 + 1]
            ) % MOD

            square[node] = (
                square[node * 2] + square[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for j, x in enumerate(nums):
            prev = last.get(x, -1)

            update(1, 0, n - 1, prev + 1, j)

            last[x] = j
            ans = (ans + square[1]) % MOD

        return ans
