class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num) // 2

        sum1 = 0
        sum2 = 0
        q1 = 0
        q2 = 0

        for i in range(n):
            if num[i] == "?":
                q1 += 1
            else:
                sum1 += int(num[i])

        for i in range(n, len(num)):
            if num[i] == "?":
                q2 += 1
            else:
                sum2 += int(num[i])

        if (sum1 - sum2) * 2 == (q2 - q1) * 9:
            return False

        return True