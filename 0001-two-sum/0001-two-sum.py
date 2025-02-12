class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        twosum = 0
        for i in range(n):
            for j in range(i+1,n):
                twosum = nums[i]+nums[j]
                if target == twosum:
                    return [i,j]