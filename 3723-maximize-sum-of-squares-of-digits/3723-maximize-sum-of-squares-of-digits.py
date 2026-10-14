# class Solution:
#     def maxSumOfSquares(self, num: int, summ: int) -> str:
#         new = []

#         if(num == 1 or num==0):
#             print('""')
#         else:
#             for i in range(len(str(num))):
#                 if(len(str(i))==num):
#                     new.append(i)
#         ans = 0
#         final = 0
#         anss = 0
#         for i in range(len(new)):
#             for j in range(len(str(i))):
#                 ans += j*j

#             final = max(final , ans)
#             anss = new[i]
#             break
#         return anss
                


class Solution:
    def maxSumOfSquares(self, num: int, summ: int) -> str:
        if summ > 9 * num:
            return ""

        ans = ""

        for i in range(num):
            digit = min(9, summ)
            ans += str(digit)
            summ -= digit



        return ans
