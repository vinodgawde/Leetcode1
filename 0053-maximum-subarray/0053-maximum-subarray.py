class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        sum1=0
        n=len(nums)
        for i in range(n):
            sum1+=nums[i]

            if sum1 > max_sum:
                max_sum = sum1
            
            if sum1 < 0:
                sum1 = 0
        return max_sum