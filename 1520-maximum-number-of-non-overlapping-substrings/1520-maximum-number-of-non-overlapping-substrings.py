class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        for i in range(n):
            c = ord(s[i]) - ord('a')

            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        for c in range(26):

            if first[c] == n:
                continue

            left = first[c]
            right = last[c]

            valid = True
            i = left

            while i <= right:
                x = ord(s[i]) - ord('a')

                if first[x] < left:
                    valid = False
                    break

                if last[x] > right:
                    right = last[x]

                i += 1

            if valid:
                intervals.append((left, right))

        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for left, right in intervals:

            if left > prev_end:
                ans.append(s[left:right + 1])
                prev_end = right

        return ans