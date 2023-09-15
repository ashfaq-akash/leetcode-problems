class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        pos=0
        neg=0

        for i in range(0,len(nums)):
            if nums[i]<0:
                neg +=1
            elif nums[i]>0:
                pos +=1
            else:
                pos=pos
                neg=neg
        if pos<neg:
            return neg
        elif pos>neg:
            return pos
        else:
            return pos

    
sol=Solution()
res=sol.maximumCount([-3,-2,-1,0,0,1,2])
print(res)
        
