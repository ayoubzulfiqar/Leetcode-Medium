import collections

class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = collections.Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.freq2[old_val] -= 1
        
        self.nums2[index] += val
        new_val = self.nums2[index]
        self.freq2[new_val] += 1

    def count(self, tot: int) -> int:
        total_pairs = 0
        for num1_val in self.nums1:
            required_num2_val = tot - num1_val
            total_pairs += self.freq2.get(required_num2_val, 0)
        return total_pairs