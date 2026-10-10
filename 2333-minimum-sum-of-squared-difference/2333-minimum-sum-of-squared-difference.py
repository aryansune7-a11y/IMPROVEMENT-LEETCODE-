class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2

            need = sum(max(0, d - mid) for d in diff)

            if need <= k:
                right = mid
            else:
                left = mid + 1

        limit = left
        ans = 0
        used = 0

        for d in diff:
            if d > limit:
                used += d - limit
                d = limit

            ans += d * d

        remaining = k - used
        ans -= remaining * (2 * limit - 1)

        return ans
