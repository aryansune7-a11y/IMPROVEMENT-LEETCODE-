class Solution:
    def maxDepth(self, s: str) -> int:
        maxcount = 0
        count = 0
        for i in range(len(s)):
            if(s[i]=="("):
                count += 1
                maxcount = max(maxcount, count)
            elif(s[i]==")"):
                count -= 1

        return maxcount