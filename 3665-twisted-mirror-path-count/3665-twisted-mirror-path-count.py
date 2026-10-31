class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7

        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        directions = [(0, 1), (1, 0)] 

        for i in range(m):
            for j in range(n):

                if dp[i][j] == 0:
                    continue

                for di, dj in directions:
                    x = i + di
                    y = j + dj

                    while 0 <= x < m and 0 <= y < n and grid[x][y] == 1:

                        if di == 0:  
                            di, dj = 1, 0 
                        else: 
                            di, dj = 0, 1

                        x += di
                        y += dj

                    if 0 <= x < m and 0 <= y < n:
                        dp[x][y] = (dp[x][y] + dp[i][j]) % MOD

        return dp[m - 1][n - 1]