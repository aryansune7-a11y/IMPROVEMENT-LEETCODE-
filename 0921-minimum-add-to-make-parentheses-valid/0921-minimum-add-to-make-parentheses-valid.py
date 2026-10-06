class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # summ1 = 0
        # summ2 = 0

        # for i in range(len(s)):
        #     if(s[i]=="("):
        #         summ1 += 1
        #     else:
        #         summ2 += 1

        # return abs(summ1 - summ2)


        # stack1 = []
        # stack2 = []

        # count = 0

        # for i in range(len(s)):
        #     if(s[i]=="("):
        #         stack1.append(s[i])

        #     else:
        #         stack2.append(s[i])

        #         if not stack1:
        #             count+=1


        #         else:
        #             stack1.pop()  
        #             count += 1


        #         if not stack2:
        #             count+=1

        #         else:
        #             stack2.pop()
        #             count+=1
        # return count






        stack = []
        count = 0


        for i in range(len(s)):
            if(s[i]=="("):
                stack.append(s[i])

            else:
                if not stack:
                    count += 1
                else:
                    stack.pop() 

        count += len(stack) 

        return count              