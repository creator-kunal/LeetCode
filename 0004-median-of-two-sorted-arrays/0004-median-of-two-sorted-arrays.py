class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_len = m + n
        half_len = (total_len + 1) // 2
        
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2
            j = half_len - i
            
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]
            
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                if total_len % 2 == 1:
                    return max(nums1_left_max, nums2_left_max)
                return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
            elif nums1_left_max > nums2_right_min:
                right = i - 1
            else:
                left = i + 1