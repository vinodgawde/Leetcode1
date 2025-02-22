class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        set1 = set()
        for i in range(n):
            for j in range(i+1,n):
                hashm={}
                for k in range(j+1,n):
                    fourth = target - (nums[i] + nums[j] + nums[k])
                    if fourth in hashm:
                        temp = tuple(sorted([nums[i],nums[j],nums[k],fourth]))
                        set1.add(temp)
                    hashm[nums[k]]=True
        return list(set1)