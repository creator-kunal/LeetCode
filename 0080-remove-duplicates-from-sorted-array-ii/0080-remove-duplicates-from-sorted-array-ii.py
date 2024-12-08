class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # valid elements
        i = 0  
         # consecutive occurrences
        count = 1 
        
        for j in range(1, len(nums)):
            if nums[j] == nums[j - 1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                i += 1
                nums[i] = nums[j]
        
        return i + 1