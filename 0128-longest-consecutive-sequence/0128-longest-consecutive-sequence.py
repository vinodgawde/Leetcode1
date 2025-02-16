class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0  
        num_set =set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                count = 1
                while (curr_num + 1) in num_set:
                    curr_num += 1
                    count += 1
                longest = max(longest, count)

        return longest

        # if not nums:
        #     return 0  

        # nums = sorted(nums)  
        # count = 1  
        # largest = 1  
        # lastsmaller = nums[0]  

        # for i in range(1, len(nums)):
        #     if nums[i] == lastsmaller:  
        #         continue
        #     elif nums[i] - 1 == lastsmaller:  
        #         count += 1
        #     else:  
        #         largest = max(largest, count)
        #         count = 1  
            
        #     lastsmaller = nums[i]  

        # largest = max(largest, count)  
        # return largest

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


        
        