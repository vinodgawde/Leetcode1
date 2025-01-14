class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_nums=list(set(nums))
        distinct_nums.sort(reverse=True)
        if len(distinct_nums)>=3:
            max=distinct_nums[2]
        else:
            max=distinct_nums[0]
        return max
