class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        low = []
        high = []

        loww = 0
        highh = 0
        
        nums.sort(key=abs)
        for i in range(len(nums)//2):
            low.append(abs(nums[i]*nums[i]))
        for i in range((len(nums)//2),len(nums)):
            high.append(abs(nums[i]*nums[i]))

        for i in range(len(low)):
            loww += low[i]
        for i in range(len(high)):
            highh += high[i]
        
        return highh-loww

        