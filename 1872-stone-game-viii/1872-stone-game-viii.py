class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        
        pref = stones.copy()
        for i in range(1, n):
            pref[i] += pref[i - 1]
            
        dp = pref[-1]
        
        for i in range(n - 2, 0, -1):
            dp = max(dp, pref[i] - dp)
            
        return dp