class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0
        base = 0
        
        while base < n:
            end = base
            
            # If base is a valid position and we have a rising slope
            if base + 1 < n and arr[base] < arr[base + 1]:
                # Find the peak
                while end + 1 < n and arr[end] < arr[end + 1]:
                    end += 1
                
                # If end is not the last element and we have a falling slope
                if end + 1 < n and arr[end] > arr[end + 1]:
                    # Find the bottom of the falling slope
                    while end + 1 < n and arr[end] > arr[end + 1]:
                        end += 1
                    
                    # end - base + 1 is the length of the mountain
                    result = max(result, end - base + 1)
            
            # Move base to the next position
            base = max(end, base + 1)
        
        return result