class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        count = {}

        for i in range(len(s)):
            if s[i] in count :
                count[s[i]] += 1
            else:
                count[s[i]] = 1

            while count[s[i]] > 2:
                count[s[left]] -= 1
                left +=1
            ans = max(ans, i-left+1)

        return ans