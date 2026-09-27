class Solution:
    def reverseParentheses(self, s: str) -> str:
        astack = []
        for i in range(len(s)):
            if (s[i]!=")"):
                astack.append(s[i])
            else:
                temp = [] 
                while astack[-1]!="(":
                    temp.append(astack.pop())
                astack.pop()

                for x in temp:
                    astack.append(x)
        return ''.join(astack)            