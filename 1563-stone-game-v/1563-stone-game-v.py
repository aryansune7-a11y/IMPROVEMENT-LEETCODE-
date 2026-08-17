class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        def solve(l, r):

            if l >= r:
                return 0

            if dp[l][r] != 0:
                return dp[l][r]

            left = 0
            right = prefix[r + 1] - prefix[l]
            ans = 0

            for k in range(l, r):

                left += stoneValue[k]
                right -= stoneValue[k]
                if left < right:

                    if ans >= left * 2:
                        continue

                    ans = max(
                        ans,
                        left + solve(l, k)
                    )
                elif left > right:

                    if ans >= right * 2:
                        break

                    ans = max(
                        ans,
                        right + solve(k + 1, r)
                    )

                else:

                    ans = max(
                        ans,
                        left + solve(l, k),
                        right + solve(k + 1, r)
                    )

            dp[l][r] = ans
            return ans

        return solve(0, n - 1)