class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ""
        summ = 0

        for ch in str(n):
            if ch != '0':
                x += ch
                summ += int(ch)

        if x == "":
            return 0

        return int(x) * summ