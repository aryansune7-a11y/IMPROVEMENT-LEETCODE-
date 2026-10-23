class Solution:
    def sortPermutation(self, nums: List[int]) -> int:

        # nums.sort()

        # ans = 0
        # new = 0

        # for i in range(len(nums)):
        #     for j in range(i):
        #         ans = nums[i] & nums[j]
        #         if ans in nums:
        #             nums[i], nums[j] = nums[j], nums[i]
        #         else:

        #             new = max(ans, new)
        #             return new
        # return ans

        ans = -1

        for i in range(len(nums)):
            if nums[i] != i:
                ans &= nums[i]

        return ans if ans != -1 else 0