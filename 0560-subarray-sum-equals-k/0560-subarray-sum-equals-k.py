class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        curr_sum=0
        count=0
        prefixsum={0:1}
        for i in range(n):
            curr_sum += nums[i]
            remove = curr_sum-k
            count += prefixsum.get(remove, 0)
            prefixsum[curr_sum] = prefixsum.get(curr_sum, 0) + 1

        return count