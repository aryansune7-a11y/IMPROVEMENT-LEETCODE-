class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if nums == sorted(nums):
            return 0
        pos0 = nums.index(0)
        s = nums[0]
        best = float('inf')
        if all(nums[i] == (s + i) % n for i in range(n)):
            k = (n - s) % n 
            best = min(best, k, s + 2) 

        if all(nums[i] == (s - i) % n for i in range(n)):
            best = min(best,
                    1 + (n - 1 - pos0),
                    (pos0 + 1) % n + 1) 

        return -1 if best == float('inf') else best