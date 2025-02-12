class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        numMap = {}
        for i in range(n):
            twosum = target - nums[i]
            if twosum in numMap:
                return [i,numMap[twosum]]
            numMap[nums[i]] = i
        return []