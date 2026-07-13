class Solution:
    def sequentialDigits(self,low, high):
        digits = "123456789"
        result = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for i in range(10 - length):
                num = int(digits[i:i + length])
                if low <= num <= high:
                    result.append(num)

        return result
