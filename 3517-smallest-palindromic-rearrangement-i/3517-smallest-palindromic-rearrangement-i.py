from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        n = len(s)

        ans = [""] * n
        left = 0
        right = n - 1

        for ch in sorted(count.keys()):
            while count[ch] >= 2:
                ans[left] = ch
                ans[right] = ch
                left += 1
                right -= 1
                count[ch] -= 2

        for ch in sorted(count.keys()):
            if count[ch] == 1:
                ans[left] = ch
                break

        return "".join(ans)