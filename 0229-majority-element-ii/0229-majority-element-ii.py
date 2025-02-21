class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            if len(ans)==0 or nums[i] not in ans:
                count = 0
                for j in range(n):
                    if nums[i]==nums[j]:
                        count+=1
                if count > n//3:
                    ans.append(nums[i])
            if len(ans) == 2:  
                break
        return ans