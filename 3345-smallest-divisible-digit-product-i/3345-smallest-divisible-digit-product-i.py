class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for _ in range(n):
            if(n<=t):
                return t
            else:

                temp = str(n)
                value = 0
                for i in range(len(temp)):
                    if(n<10):
                        value = n

                    elif(n==100):
                        value = n
                        return n
                    else:
                        value = int(temp[0])*int(temp[1])
                if(value%t==0):
                    return n 
                n += 1

