class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def solve(arr):
            if len(arr) <= 2:
                return 1

            left = [x for x in arr if x < arr[0]]
            right = [x for x in arr if x > arr[0]]

            ways = math.comb(len(left) + len(right), len(left))

            return ways * solve(left) * solve(right) % MOD

        return (solve(nums) - 1) % MOD
