class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])

        arr = []
        for row in grid:
            arr.extend(row)

        k %= len(arr)
        arr = arr[-k:] + arr[:-k]

        ans = []
        idx = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(arr[idx])
                idx += 1
            ans.append(row)

        return ans