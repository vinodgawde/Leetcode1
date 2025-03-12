class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        pos_max = 0 
        neg_max = 0
        for i in range(n):
            if nums[i] < 0:
                neg_max += 1
            if nums[i] > 0:
                pos_max +=1
        return max(pos_max,neg_max) 