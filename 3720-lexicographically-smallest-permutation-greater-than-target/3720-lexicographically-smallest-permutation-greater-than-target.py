class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        n = len(s)

        # Characters used by the equal prefix
        used = [0] * n

        # Match target from left to right
        i = 0

        while i < n:
            x = ord(target[i]) - ord('a')

            if cnt[x] == 0:
                break

            cnt[x] -= 1
            used[i] = 1
            i += 1

        # Try changing the current position or an earlier position
        for pos in range(i, -1, -1):

            # If pos == i, all characters before pos are already used.
            # If pos < i, restore target[pos].
            if pos < i:
                x = ord(target[pos]) - ord('a')
                cnt[x] += 1

            # If pos == n, there is no character to change
            if pos >= n:
                continue

            x = ord(target[pos]) - ord('a')

            # Find smallest character greater than target[pos]
            for c in range(x + 1, 26):
                if cnt[c] > 0:

                    cnt[c] -= 1

                    ans = target[:pos] + chr(c + ord('a'))

                    # Remaining characters in sorted order
                    for k in range(26):
                        ans += chr(k + ord('a')) * cnt[k]

                    return ans

        return ""