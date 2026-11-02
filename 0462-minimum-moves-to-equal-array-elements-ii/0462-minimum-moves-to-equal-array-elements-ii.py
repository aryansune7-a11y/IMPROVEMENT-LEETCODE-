class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid = len(nums) // 2
        ans = 0

        for i in nums:
            ans += abs(i - nums[mid])

        return ans