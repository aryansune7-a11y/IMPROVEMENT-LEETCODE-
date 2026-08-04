class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        new = []

        for i in range(len(nums) - 1):
            for j in range(nums[i] + 1, nums[i + 1]):
                new.append(j)

        return new  