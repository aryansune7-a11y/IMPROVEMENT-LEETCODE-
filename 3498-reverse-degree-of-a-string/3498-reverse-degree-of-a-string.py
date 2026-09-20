class Solution:
    def reverseDegree(self, s: str) -> int:
        newsum = 0

        def value(ch):
            return 26 - (ord(ch) - ord('a'))

        j = 1

        for i in s:
            newsum += value(i) * j
            j += 1

        return newsum