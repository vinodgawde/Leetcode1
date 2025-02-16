class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=0
        largest=0
        lastsmaller = float('-inf')
        nums=sorted(nums)
        n=len(nums)
        for i in range(n):
            if (nums[i]-1) == lastsmaller:
                count+=1
                lastsmaller = nums[i]
            elif nums[i] != lastsmaller:
                count=1
                lastsmaller = nums[i]
            largest = max(largest, count)
        return largest

# class Solution:
#     def liner(self, nums, x):
#         n= len(nums)
#         for i in range(n):
#             if nums[i]==x:
#                 return True
#         return False

#     def longestConsecutive(self, nums: List[int]) -> int:
#         longest = 1
#         n= len(nums)
#         if not nums:
#             return 0 
#         for i in range(n):
#             x=nums[i]
#             count=1
#             while self.liner(nums, x + 1):
#                 x=x+1
#                 count+=1
#             longest = max(longest, count)  
        
#         return longest


        
        