class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # three pointers technique
        # 1. Initialize two pointers, and each pointer points at the last index of each List. Intialize another pointer at the inserted_index which is equal to (m + n - 1) where m, n are lengths of nums1, nums2 respectively
        # 2. Since length of nums2 must be less than or equal to nums1's length, we do a while loop as long as p2 >= 0, we check if: 
        #   - if nums[p1] > nums[p2], we insert nums[p1] into nums[inserted_index] and move inserted_index to the right. Move p1 to the left by 1. Similarly, do it for p2 

        p1, p2 = m - 1, n - 1
        inserted_index = m + n - 1
        
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[inserted_index] = nums1[p1]
                p1 -= 1
            else:
                nums1[inserted_index] = nums2[p2]
                p2 -= 1
            inserted_index -= 1
        # time: O(m + n), m, n are lengths of nums1, nums2 respectively
        # space: O(1)
        
        