class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hashM={}
        ans = []
        count = 0
        for i in range(n):
            hashM[nums[i]] = hashM.get(nums[i],0)+1
            if hashM[nums[i]] == (n//3)+1:
                ans.append(nums[i])

        return ans