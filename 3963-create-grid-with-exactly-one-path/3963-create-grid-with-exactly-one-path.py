# from typing import List

class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        return [
            ''.join('.' if i == 0 or j == n - 1 else '#'
                    for j in range(n))
            for i in range(m)
        ]

        # grid = []

        # for i in range(m):
        #     row = ""

        #     for j in range(n):
        #         if (i == 0 and j >= 2) or (j == 0 and i >= 1):
        #             row += '#'
        #         elif i >= 2 and j < n - 1:
        #             row += '#'
        #         else:
        #             row += '.'

        #     grid.append(row)

        # return grid