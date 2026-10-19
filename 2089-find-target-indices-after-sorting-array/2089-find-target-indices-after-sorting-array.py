class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        new = []
        nums.sort()
        for i in range(len(nums)):
            if(nums[i]==target):
                new.append(i)

        return new