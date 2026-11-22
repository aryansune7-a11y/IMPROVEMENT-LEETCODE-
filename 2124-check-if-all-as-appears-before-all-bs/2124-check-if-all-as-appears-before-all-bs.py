class Solution:
    def checkString(self, s: str) -> bool:
        count = 0

        for i in range(len(s)-1):

            if(s[i]=="b"):
                if(s[i+1]=="a"):
                    count += 1
        if(count != 0):
            return False
        return True