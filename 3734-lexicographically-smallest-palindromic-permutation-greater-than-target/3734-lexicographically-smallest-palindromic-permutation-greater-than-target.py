from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        
        odd = [c for c, f in cnt.items() if f % 2 == 1]
        if len(odd) > 1:
            return ""
        
        mid_char = odd[0] if odd else ""
        
        half_cnt = {c: f // 2 for c, f in cnt.items()}
        m = n // 2
        
        def solve():
            for i in range(m, -1, -1):
                cur_cnt = half_cnt.copy()
                possible = True
                
                for j in range(i):
                    c = target[j]
                    if cur_cnt.get(c, 0) <= 0:
                        possible = False
                        break
                    cur_cnt[c] -= 1
                
                if not possible:
                    continue
                
                if i == m:
                    left = target[:m]
                    pal = left + mid_char + left[::-1] if n % 2 else left + left[::-1]
                    if pal > target:
                        return pal
                    continue
                
                target_char = target[i]
                
                for c in sorted(cur_cnt.keys()):
                    if c > target_char and cur_cnt[c] > 0:
                        cur_cnt[c] -= 1
                        rem = []
                        for ch in sorted(cur_cnt.keys()):
                            rem.extend([ch] * cur_cnt[ch])
                        
                        left = target[:i] + c + "".join(rem)
                        return left + mid_char + left[::-1] if n % 2 else left + left[::-1]
            
            return ""

        return solve()