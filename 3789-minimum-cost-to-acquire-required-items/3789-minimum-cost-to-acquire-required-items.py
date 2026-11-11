class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        common = min(need1, need2)

        ans = common * min(costBoth, cost1 + cost2)

        ans += (need1 - common) * min(cost1, costBoth)
        ans += (need2 - common) * min(cost2, costBoth)

        return ans