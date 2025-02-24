class Solution:
    def lowerbound(self, nums, target):
        n=len(nums)
        low = 0
        high = n-1
        ans = n
        while(low<=high):
            mid = (low + high) // 2
            if (nums[mid] >= target ):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans 

    def upperbound(self, nums, target):
        n=len(nums)
        low = 0
        high = n-1
        ans = n
        while(low<=high):
            mid = (low + high) // 2
            if (nums[mid] > target ):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans 

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lowerbound(nums, target)
        if (lb == len(nums) or nums[lb] != target):
            return [-1,-1]
        return [lb,self.upperbound(nums, target)-1]