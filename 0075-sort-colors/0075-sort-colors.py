class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count1=0
        count2=0
        count3=0
        for i in range(len(nums)):
            if nums[i]==0:
                count1+=1
            if nums[i]==1:
                count2+=1
            if nums[i]==2:
                count3+=1
        for i in range(count1):
            nums[i]=0
        for i in range(count1,count1+count2):
            nums[i]=1
        for i in range(count1+count2,count1+count2+count3):
            nums[i]=2