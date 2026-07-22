class Solution:
    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)
        NEG, POS = float('-inf'), float('inf')

        # 1. build runs
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], i, j - 1))
            i = j
        m = len(runs)
        lens = [en - st + 1 for (_, st, en) in runs]

        pos2run = [0] * n
        for idx, (_, st, en) in enumerate(runs):
            for p in range(st, en + 1):
                pos2run[p] = idx

        total1 = s.count('1')

        vArr = [NEG] * m
        zeroArr = [NEG] * m
        oneArr = [POS] * m
        for k in range(m):
            c = runs[k][0]
            if c == '0':
                zeroArr[k] = lens[k]
            else:
                oneArr[k] = lens[k]
            if 1 <= k <= m - 2 and c == '1':
                vArr[k] = lens[k - 1] + lens[k + 1]

        def build_max(arr):
            L = len(arr)
            if L == 0:
                return []
            st = [arr[:]]
            j = 1
            while (1 << j) <= L:
                prev = st[-1]
                half = 1 << (j - 1)
                length = L - (1 << j) + 1
                cur = [max(prev[i2], prev[i2 + half]) for i2 in range(length)]
                st.append(cur)
                j += 1
            return st

        def build_min(arr):
            L = len(arr)
            if L == 0:
                return []
            st = [arr[:]]
            j = 1
            while (1 << j) <= L:
                prev = st[-1]
                half = 1 << (j - 1)
                length = L - (1 << j) + 1
                cur = [min(prev[i2], prev[i2 + half]) for i2 in range(length)]
                st.append(cur)
                j += 1
            return st

        def q_max(st, l, r):
            if l > r:
                return NEG
            k = (r - l + 1).bit_length() - 1
            return max(st[k][l], st[k][r - (1 << k) + 1])

        def q_min(st, l, r):
            if l > r:
                return POS
            k = (r - l + 1).bit_length() - 1
            return min(st[k][l], st[k][r - (1 << k) + 1])

        stV = build_max(vArr)
        stZeroMax = build_max(zeroArr)
        stOneMin = build_min(oneArr)

        ans = []
        for l, r in queries:
            idx_l = pos2run[l]
            idx_r = pos2run[r]

            if idx_l == idx_r:
                ans.append(total1)
                continue

            c_l, st_l, en_l = runs[idx_l]
            c_r, st_r, en_r = runs[idx_r]
            clipped_l = en_l - l + 1
            clipped_r = r - st_r + 1

            k0, k1 = idx_l + 1, idx_r - 1
            if k0 > k1:
                ans.append(total1)
                continue

            minOne = q_min(stOneMin, k0, k1)
            if minOne == POS:
                ans.append(total1)
                continue

            zc_l = clipped_l if c_l == '0' else NEG
            zc_r = clipped_r if c_r == '0' else NEG
            zmid = q_max(stZeroMax, k0, k1)
            maxZero = max(zc_l, zc_r, zmid)
            term2 = maxZero - minOne

            if k0 == k1:
                term1 = clipped_l + clipped_r
            else:
                cands = []
                if runs[k0][0] == '1':
                    cands.append(clipped_l + lens[k0 + 1])
                if runs[k1][0] == '1':
                    cands.append(lens[k1 - 1] + clipped_r)
                if k0 + 1 <= k1 - 1:
                    cands.append(q_max(stV, k0 + 1, k1 - 1))
                term1 = max(cands) if cands else NEG

            gain = max(term1, term2, 0)
            ans.append(total1 + gain)

        return ans