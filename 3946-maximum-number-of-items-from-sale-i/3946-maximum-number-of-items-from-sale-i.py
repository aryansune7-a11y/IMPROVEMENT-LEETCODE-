class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        n = len(items)

        benefits = [1] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    benefits[i] += 1

        arr = sorted(
            [(items[i][1], benefits[i]) for i in range(n)],
            reverse=True
        )

        dp = [-1] * (budget + 1)
        dp[0] = 0

        ans = 0
        k = 0

        while k < n:

            p = arr[k][0]
            dpP = [-1] * (budget + 1)

            while k < n and arr[k][0] == p:

                price, benefit = arr[k]

                for c in range(budget, price - 1, -1):

                    if dp[c - price] != -1:
                        dpP[c] = max(
                            dpP[c],
                            dp[c - price] + benefit
                        )

                    if dpP[c - price] != -1:
                        dpP[c] = max(
                            dpP[c],
                            dpP[c - price] + benefit
                        )
                    if dp[c - price] != -1:
                        dp[c] = max(
                            dp[c],
                            dp[c - price] + benefit
                        )

                k += 1

            for c in range(budget + 1):

                if dpP[c] != -1:

                    extra = (budget - c) // p

                    ans = max(ans, dpP[c] + extra)

        return ans
