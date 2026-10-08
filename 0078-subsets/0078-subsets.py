class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        new = []
        ans = []

        def final(nums, i, new):
            if i == len(nums):
                ans.append(new.copy())
                return

            final(nums, i + 1, new)

            new.append(nums[i])

            final(nums, i + 1, new)

            new.pop()



        final(nums, 0, new)

        return ans