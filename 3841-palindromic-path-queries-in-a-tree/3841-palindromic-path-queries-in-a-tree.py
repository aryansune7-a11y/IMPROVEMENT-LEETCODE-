class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        s = list(s)
        LOG = n.bit_length()

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        # Iterative DFS
        stack = [(0, 0, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = p
                tin[u] = timer
                timer += 1

                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        # Binary lifting
        up = [parent]

        for j in range(1, LOG):
            prev = up[j - 1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        # Fenwick Tree using XOR
        bit = [0] * (n + 2)

        def update(i, val):
            i += 1
            while i < len(bit):
                bit[i] ^= val
                i += i & -i

        def prefix(i):
            ans = 0
            i += 1

            while i > 0:
                ans ^= bit[i]
                i -= i & -i

            return ans

        # Each character affects its entire subtree
        for u in range(n):
            mask = 1 << (ord(s[u]) - ord('a'))
            update(tin[u], mask)
            update(tout[u], mask)

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old = 1 << (ord(s[u]) - ord('a'))
                new = 1 << (ord(c) - ord('a'))

                if old != new:
                    change = old ^ new
                    update(tin[u], change)
                    update(tout[u], change)
                    s[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                mask_u = prefix(tin[u])
                mask_v = prefix(tin[v])
                mask_w = 1 << (ord(s[w]) - ord('a'))

                mask = mask_u ^ mask_v ^ mask_w

                ans.append((mask & (mask - 1)) == 0)

        return ans