class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c1=0
        c2=0
        c3=0
        for i in range(len(nums)):
            if nums[i]==0:
                c1+=1
            if nums[i]==1:
                c2+=1
            if nums[i]==2:
                c3+=1
        for i in range(c1):
            nums[i]=0
        for i in range(c1,c1+c2):
            nums[i]=1
        for i in range(c1+c2,c1+c2+c3):
            nums[i]=2