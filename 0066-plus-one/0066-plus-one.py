class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        new = ""

        for i in range(len(digits)):
            new += str(digits[i])

        final = int(new)
        ans = final + 1

        neew = str(ans)

        finall = []
        for i in range(len(neew)):
            finall.append(int(neew[i]))

        return finall