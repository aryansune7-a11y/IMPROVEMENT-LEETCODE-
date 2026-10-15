# class Solution:
#     def sumCounts(self, nums: List[int]) -> int:
#         new = [[]]

#         final = {}

#         now = []
#         ans = 0
#         for i in range(len(nums)):
#             for j in range(i):
#                 new.append(nums[j])

#                 set.final{}

#             now.append(len(final))

#         for i in range(len(now)):
#             ans += now[i]*now[i]


#         return ans

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            final = set()

            for j in range(i, n):
                final.add(nums[j])
                ans += len(final) * len(final)

        return ans
