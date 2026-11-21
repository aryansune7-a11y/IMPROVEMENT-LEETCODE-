class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        n = len(parent)

        tree = [[] for _ in range(n)]

        for i in range(1, n):
            tree[parent[i]].append(i)

        new_parent = parent[:]
        last = {}

        def dfs(node):
            ch = s[node]

            old = last.get(ch)

            if old is not None:
                new_parent[node] = old

            last[ch] = node

            for child in tree[node]:
                dfs(child)

            if old is None:
                del last[ch]
            else:
                last[ch] = old

        dfs(0)

        new_tree = [[] for _ in range(n)]

        for i in range(1, n):
            new_tree[new_parent[i]].append(i)

        ans = [0] * n

        def calculate(node):
            ans[node] = 1

            for child in new_tree[node]:
                ans[node] += calculate(child)

            return ans[node]

        calculate(0)

        return ans
