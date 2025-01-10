class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        #binary search
        while left <= right:
            #middle index
            mid = (left + right) // 2
            
            #target is found
            if nums[mid] == target:
                return mid
            
            #target is greater
            if nums[mid] < target:
                left = mid + 1
            
            #target is smaller
            else:
                right = mid - 1
        
        return left