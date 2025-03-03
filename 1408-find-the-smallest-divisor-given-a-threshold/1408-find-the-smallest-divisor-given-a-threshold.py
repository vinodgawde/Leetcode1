class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        while(low <= high):
            mid = low + (high - low) // 2
            sum1 = 0
            for i in range(len(nums)):
                sum1 += math.ceil(nums[i]/mid)
            if sum1 <= threshold:
                high = mid - 1
            else:
                low = mid + 1
            
        return low