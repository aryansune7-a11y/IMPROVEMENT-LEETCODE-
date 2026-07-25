class Solution:
    def maxProduct(self, n: int) -> int:

        digits = [int(d) for d in str(n)]

        largest = second = 0

        for d in digits:
            if d > largest:
                second = largest
                largest = d
            elif d > second:
                second = d

        return largest * second