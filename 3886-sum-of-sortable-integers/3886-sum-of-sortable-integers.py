
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        ans = 0

        def check(a, b):
            k = len(a)

            # Build KMP prefix array
            lps = [0] * k
            j = 0

            for i in range(1, k):
                while j > 0 and b[i] != b[j]:
                    j = lps[j - 1]

                if b[i] == b[j]:
                    j += 1
                    lps[i] = j

            # Search b in a+a, allowing only k rotations
            j = 0

            for i in range(2 * k - 1):
                x = a[i % k]

                while j > 0 and x != b[j]:
                    j = lps[j - 1]

                if x == b[j]:
                    j += 1

                if j == k:
                    return True

            return False

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            ok = True

            for i in range(0, n, k):
                if not check(nums[i:i + k], target[i:i + k]):
                    ok = False
                    break

            if ok:
                ans += k

        return ans
