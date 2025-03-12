class Solution:
    def lowerbound(self,nums):
        ind = len(nums)
        low = 0
        high = len(nums) - 1 
        while(low <= high):
            mid = low + (high - low) // 2
            if nums[mid] >= 0:
                ind = mid
                high = mid - 1
            else:
                low = mid + 1
        return ind

    def upperbound(self,nums):
        ind = len(nums)
        low = 0
        high = len(nums) - 1 
        while(low <= high):
            mid = low + (high - low) // 2
            if nums[mid] > 0:
                ind = mid
                high = mid - 1
            else:
                low = mid + 1
        return ind

    def maximumCount(self, nums: List[int]) -> int:
        pos_max = len(nums) - self.upperbound(nums)
        neg_max = self.lowerbound(nums)
        return max(pos_max,neg_max) 