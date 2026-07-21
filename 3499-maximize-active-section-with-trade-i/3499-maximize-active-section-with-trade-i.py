class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"
        n = len(t)

        active = s.count('1')
        ans = active

        i = 0
        while i < n:
            if t[i] == '1':
                j = i
                while j < n and t[j] == '1':
                    j += 1

                if i > 0 and j < n and t[i - 1] == '0' and t[j] == '0':

                    l = i - 1
                    while l >= 0 and t[l] == '0':
                        l -= 1
                    leftZeros = i - l - 1

                    r = j
                    while r < n and t[r] == '0':
                        r += 1
                    rightZeros = r - j

                    ans = max(ans, active + leftZeros + rightZeros)

                i = j
            else:
                i += 1

        return ans