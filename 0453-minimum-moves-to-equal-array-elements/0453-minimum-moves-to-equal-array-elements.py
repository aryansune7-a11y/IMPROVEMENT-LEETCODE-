class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # new = set(nums)
        # neww = sorted(nums)
        # if(len(new)==1):
        #     return 0
        # else:
        #     count = 0
        #     n = len(nums)
        #     while len(set(neww))!=1:

        #         for i in range(n-1):
        #             neww = sorted(nums)
        #             neww[i] = neww[i]+1
        #             count += 1
        #     return count
            
        mini = min(nums)
        count = 0

        for i in nums:
            count += i - mini

        return count

