class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        nums.sort()

        m = max(nums)

        for i in range(len(nums)):
            count += abs(nums[i] - m)

        return count