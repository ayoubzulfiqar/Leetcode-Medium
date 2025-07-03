class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums1)
        
        nums1.sort()
        
        indexed_nums2 = sorted([(val, idx) for idx, val in enumerate(nums2)])
        
        result = [0] * n
        
        left_nums1_ptr = 0  # Pointer for the smallest available element in nums1
        left_nums2_ptr = 0  # Pointer for the smallest target element in indexed_nums2
        right_nums2_ptr = n - 1 # Pointer for the largest target element in indexed_nums2
        
        while left_nums2_ptr <= right_nums2_ptr:
            # Get the smallest remaining nums2 element and its original index
            b_val, b_idx = indexed_nums2[left_nums2_ptr]
            
            # If the smallest available nums1 element can beat the smallest available nums2 element
            if nums1[left_nums1_ptr] > b_val:
                # Assign this nums1 element to beat nums2[b_idx]
                result[b_idx] = nums1[left_nums1_ptr]
                left_nums1_ptr += 1  # Move to the next smallest nums1 element
                left_nums2_ptr += 1  # Move to the next smallest nums2 element (it's now matched)
            else:
                # If the smallest available nums1 element cannot beat the smallest available nums2 element,
                # it means this nums1 element cannot beat any of the remaining nums2 elements
                # (since nums2 elements are sorted in ascending order).
                # In this case, we must "waste" this nums1 element. We assign it to the largest remaining nums2 element.
                # This strategy saves potentially useful larger nums1 elements for smaller nums2 elements that might be beatable.
                
                # Get the largest remaining nums2 element and its original index
                largest_b_val, largest_b_idx = indexed_nums2[right_nums2_ptr]
                
                result[largest_b_idx] = nums1[left_nums1_ptr] # Assign the current smallest nums1 element
                left_nums1_ptr += 1  # Move to the next smallest nums1 element
                right_nums2_ptr -= 1 # Move to the next largest nums2 element (it's now "used")
                
        return result