class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minimum = min(nums1)

        if minimum % 2 == 1:
            return True

        for num in nums1:
            if num % 2 == 1:
                return False

        return True