class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        
        for i in range(len(nums)//2):
            nums[2*i]=pos[i]
            nums[2*i+1]=neg[i]

        return nums