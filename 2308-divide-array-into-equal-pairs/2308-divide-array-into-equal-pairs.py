class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()
        for i in range(0,n,2):
            if nums[i] != nums[i + 1]:
                return False
        return True