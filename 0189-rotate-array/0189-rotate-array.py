class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        
        # reverse portion of array
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # reverse entire array
        reverse(0, n - 1)
        # reverse first k elements
        reverse(0, k - 1)
        # reverse remaining n-k elements
        reverse(k, n - 1)

