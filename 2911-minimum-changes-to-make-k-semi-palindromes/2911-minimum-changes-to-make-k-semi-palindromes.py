class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):

                length = j - i + 1
                best = float('inf')

                for d in range(1, length):

                    if length % d != 0:
                        continue

                    changes = 0

                    for t in range(d):

                        left = i + t
                        right = j - ((length - 1 - t) % d)

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[i][j] = best

        INF = float('inf')

        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        dp[0][0] = 0

        for parts in range(1, k + 1):

            for i in range(2 * parts, n + 1):

                for x in range(2 * (parts - 1), i - 1):

                    dp[i][parts] = min(
                        dp[i][parts],
                        dp[x][parts - 1] + cost[x][i - 1]
                    )

        return dp[n][k]
