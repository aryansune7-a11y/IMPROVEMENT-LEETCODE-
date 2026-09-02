class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if(len(nums1)<=1):
            return True
        else:
                
            for i in range(len(nums1)-1):
                if((nums1[i]%2==0 and nums1[i+1]%2==0) or (nums1[i]%2!=0 and nums1[i+1]%2!=0)):
                    return True
                else:    
                    new = nums1[i]- nums1[i+1]
                    if(new%2!=0):
                        return True
                    else:
                        return False    
