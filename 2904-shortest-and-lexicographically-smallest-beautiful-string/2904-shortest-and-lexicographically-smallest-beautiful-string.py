class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        min_len = float('inf')

        for i in range(len(s)):
            count = 0

            for j in range(i, len(s)):
                if s[j] == '1':
                    count += 1

                if count == k:
                    sub = s[i:j+1]

                    if len(sub) < min_len:
                        min_len = len(sub)
                        ans = sub

                    elif len(sub) == min_len and sub < ans:
                        ans = sub

                    break

        return ans