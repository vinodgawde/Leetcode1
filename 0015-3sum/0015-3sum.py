class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        set1 = set()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            hashm = {}
            for j in range(i + 1, n):
                third = -(nums[i] + nums[j])
                if third in hashm:
                    set1.add(tuple(sorted([nums[i], nums[j], third])))
                hashm[nums[j]] = True 
        
        return list(set1)