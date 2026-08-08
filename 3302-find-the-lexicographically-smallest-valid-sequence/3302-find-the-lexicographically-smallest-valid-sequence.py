class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        suf = [-1] * m

        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                suf[j] = i
                j -= 1

        ans = []
        j = 0
        used = False
        start = 0

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
                continue

            if not used:
                if j == m - 1 or suf[j + 1] > i:
                    ans.append(i)
                    used = True
                    j += 1

        if j == m:
            return ans

        return []