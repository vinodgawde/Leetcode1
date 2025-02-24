class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        n= len(nums)
        ans = n
        while low <= high:
            mid = low + (high - low) // 2 
            if nums[mid] >= target:
                ans = mid
                high = mid-1
            else:
                low=mid+1
        return ans