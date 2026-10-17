class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        update = []

        for i in range(len(nums)):
            up = 0
            for j in range(len(str(nums[i]))):
                up += int(str(nums[i])[j])
            update.append((up, nums[i], i))

        target = sorted(update)
        visited = [False] * len(nums)
        count = 0

        for i in range(len(nums)):
            if visited[i] or target[i][2] == i:
                continue

            j = i
            cycle = 0

            while not visited[j]:
                visited[j] = True
                j = target[j][2]
                cycle += 1

            count += cycle - 1

        return count