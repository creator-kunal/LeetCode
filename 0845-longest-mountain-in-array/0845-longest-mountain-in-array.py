class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:  # Mountain needs at least 3 elements
            return 0
        
        max_length = 0
        i = 1
        
        # One-pass solution with O(1) space
        while i < n:
            # Skip flat areas
            if i < n - 1 and arr[i-1] == arr[i]:
                i += 1
                continue
            
            # Check for upslope
            up_count = 0
            while i < n and arr[i-1] < arr[i]:
                up_count += 1
                i += 1
            
            # Check for downslope
            down_count = 0
            while i < n and arr[i-1] > arr[i]:
                down_count += 1
                i += 1
            
            # If we have both upslope and downslope, we have a mountain
            if up_count > 0 and down_count > 0:
                max_length = max(max_length, up_count + down_count + 1)
        
        return max_length