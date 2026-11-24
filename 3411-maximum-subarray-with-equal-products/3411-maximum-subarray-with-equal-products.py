
import math
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            prod = 1
            g = 0
            l = 1

            for j in range(i, len(nums)):
                prod *= nums[j]
                g = math.gcd(g, nums[j])
                l = math.lcm(l, nums[j])

                if prod == g * l:
                    count = max(count, j - i + 1)

        return count
