class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        mod1 = 10**9 + 7
        mod2 = 10**9 + 9
        base = 911382323

        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)

        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)

        for i in range(n):
            x = nums[i] + 1

            h1[i + 1] = (h1[i] * base + x) % mod1
            h2[i + 1] = (h2[i] * base + x) % mod2

            p1[i + 1] = p1[i] * base % mod1
            p2[i + 1] = p2[i] * base % mod2

        def check(k):
            freq = {}

            for i in range(n - k + 1):
                j = i + k

                a = (h1[j] - h1[i] * p1[k]) % mod1
                b = (h2[j] - h2[i] * p2[k]) % mod2

                key = (a, b)

                freq[key] = freq.get(key, 0) + 1

                if freq[key] == 1:
                    pass

            return 1 in freq.values()

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
