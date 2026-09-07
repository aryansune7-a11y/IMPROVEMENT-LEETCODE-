class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        dp = 0
        last = {}

        for ch in s:
            new_dp = 2 * dp + 1

            if ch in last:
                new_dp -= last[ch]

            last[ch] = dp + 1
            dp = new_dp % MOD

        return dp
        