class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:

        n = len(s)

        palindrome = [[False] * n for _ in range(n)]

        for i in range(n):
            palindrome[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):

                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2:
                        palindrome[i][j] = True
                    else:
                        palindrome[i][j] = palindrome[i + 1][j - 1]

        dp = [0] * (n + 1)

        for i in range(1, n + 1):

            dp[i] = dp[i - 1]

            for j in range(i):

                length = i - j

                if length >= k and palindrome[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]