class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree_prod = [1] * (4 * n)
        tree_counts = [[0] * k for _ in range(4 * n)]
        
        def merge(node, left_child, right_child):
            tree_prod[node] = (tree_prod[left_child] * tree_prod[right_child]) % k
            
            c = list(tree_counts[left_child])
            lp = tree_prod[left_child]
            for r in range(k):
                cnt = tree_counts[right_child][r]
                if cnt > 0:
                    c[(lp * r) % k] += cnt
            tree_counts[node] = c

        def build(node, l, r):
            if l == r:
                rem = nums[l] % k
                tree_prod[node] = rem
                tree_counts[node] = [0] * k
                tree_counts[node][rem] = 1
                return
            
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            merge(node, 2 * node, 2 * node + 1)

        def update(node, l, r, idx, val):
            if l == r:
                rem = val % k
                tree_prod[node] = rem
                tree_counts[node] = [0] * k
                tree_counts[node][rem] = 1
                return
            
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, r, idx, val)
            merge(node, 2 * node, 2 * node + 1)

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree_prod[node], tree_counts[node]
            
            mid = (l + r) // 2
            if qr <= mid:
                return query(2 * node, l, mid, ql, qr)
            if ql > mid:
                return query(2 * node + 1, mid + 1, r, ql, qr)
            
            lp, lc = query(2 * node, l, mid, ql, qr)
            rp, rc = query(2 * node + 1, mid + 1, r, ql, qr)
            
            combined_prod = (lp * rp) % k
            combined_counts = list(lc)
            for r_rem in range(k):
                cnt = rc[r_rem]
                if cnt > 0:
                    combined_counts[(lp * r_rem) % k] += cnt
                    
            return combined_prod, combined_counts

        build(1, 0, n - 1)
        ans = []
        
        for idx, val, start, target_x in queries:
            update(1, 0, n - 1, idx, val)
            _, counts = query(1, 0, n - 1, start, n - 1)
            ans.append(counts[target_x])
            
        return ans