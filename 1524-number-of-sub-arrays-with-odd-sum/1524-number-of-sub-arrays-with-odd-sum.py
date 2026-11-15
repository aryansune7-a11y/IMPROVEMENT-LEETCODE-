class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd = 0
        even = 1
        total = 0
        count = 0
        mod = 10**9 + 7

        for num in arr:
            total += num

            if total % 2 == 0:
                count += odd
                even += 1
            else:
                count += even
                odd += 1

        return count % mod