class Solution:
    def digitSum(self, s: str, k: int) -> str:
 
        while len(s) > k:
            ans = ""

            for i in range(0, len(s), k):
                sadhy = s[i:i+k]

                total = 0
                for j in sadhy:
                    total += int(j)

                ans += str(total)

            s = ans

        return s