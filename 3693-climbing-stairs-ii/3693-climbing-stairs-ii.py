class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        def solve(i, n, costs, dp):

            if i == n:
                return 0

            if dp[i] != -1:
                return dp[i]

            ans = float('inf')

            for j in range(i + 1, min(i + 3, n) + 1):

                cost = costs[j - 1] + (j - i) ** 2

                ans = min(ans, cost + solve(j, n, costs, dp))

            dp[i] = ans
            return dp[i]


        dp = [-1] * (n + 1)
        return solve(0, n, costs, dp)