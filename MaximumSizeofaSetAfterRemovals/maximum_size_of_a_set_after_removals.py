class Solution:
    def maximumSetSize(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        n_half = n // 2

        set1 = set(nums1)
        set2 = set(nums2)

        unique1 = set1 - set2
        unique2 = set2 - set1
        common = set1.intersection(set2)

        max_set_size = 0

        # Elements unique to nums1
        # We can take at most n_half elements from nums1
        # And at most len(unique1) distinct unique1 elements exist
        num_to_take_from_unique1 = min(len(unique1), n_half)
        max_set_size += num_to_take_from_unique1
        
        # Remaining slots in nums1 for common elements
        remaining_slots_in_nums1 = n_half - num_to_take_from_unique1

        # Elements unique to nums2
        # We can take at most n_half elements from nums2
        # And at most len(unique2) distinct unique2 elements exist
        num_to_take_from_unique2 = min(len(unique2), n_half)
        max_set_size += num_to_take_from_unique2
        
        # Remaining slots in nums2 for common elements
        remaining_slots_in_nums2 = n_half - num_to_take_from_unique2

        # Common elements
        # We have remaining_slots_in_nums1 + remaining_slots_in_nums2 total slots for common elements
        # And len(common) distinct common elements exist
        num_to_take_from_common = min(len(common), remaining_slots_in_nums1 + remaining_slots_in_nums2)
        max_set_size += num_to_take_from_common

        return max_set_size

```python
class Solution:
    def maximumSetSize(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        n_half = n // 2

        set1 = set(nums1)
        set2 = set(nums2)

        unique1 = set1 - set2
        unique2 = set2 - set1
        common = set1.intersection(set2)

        max_set_size = 0

        # Elements unique to nums1
        num_to_take_from_unique1 = min(len(unique1), n_half)
        max_set_size += num_to_take_from_unique1
        
        remaining_slots_in_nums1 = n_half - num_to_take_from_unique1

        # Elements unique to nums2
        num_to_take_from_unique2 = min(len(unique2), n_half)
        max_set_size += num_to_take_from_unique2
        
        remaining_slots_in_nums2 = n_half - num_to_take_from_unique2

        # Common elements
        num_to_take_from_common = min(len(common), remaining_slots_in_nums1 + remaining_slots_in_nums2)
        max_set_size += num_to_take_from_common

        return max_set_size

```