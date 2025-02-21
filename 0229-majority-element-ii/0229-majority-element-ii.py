class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1=0
        count2=0
        ele1=float('-inf')
        ele2=float('-inf')
        for i in range(len(nums)):
            if count1==0 and ele2 != nums[i]:
                count1=1
                ele1=nums[i]
            elif count2==0 and ele1 != nums[i]:
                count2=1
                ele2=nums[i]
            elif ele1 == nums[i]:
                count1 += 1
            elif ele2 == nums[i]:
                count2 += 1
            else:
                count1-=1
                count2-=1
        ans=[]
        count1=0
        count2=0
        for i in range(len(nums)):
            if ele1 == nums[i]:
                count1+=1
            if ele2 == nums[i]:
                count2+=1
        
        mini = (len(nums)//3)+1
        if count1 >= mini:
            ans.append(ele1)
        if count2 >= mini:
            ans.append(ele2)

        return ans