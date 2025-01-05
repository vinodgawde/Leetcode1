class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp = 0
        s1=0
        for i in range(len(nums)):
            if nums[i]==1:
                s1+=1
                if temp<=s1:
                    temp=s1
            else:
                s1=0
        return temp
        