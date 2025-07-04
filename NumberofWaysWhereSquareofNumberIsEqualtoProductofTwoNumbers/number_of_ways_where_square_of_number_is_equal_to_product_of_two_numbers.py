from collections import Counter

class Solution:
    def count_pairs_from_array(self, arr: list[int], target_product: int) -> int:
        freq_map = Counter(arr)
        count = 0
        
        unique_sorted_nums = sorted(freq_map.keys())

        for x in unique_sorted_nums:
            if target_product % x == 0:
                y = target_product // x
                
                if y in freq_map:
                    if x == y:
                        count += freq_map[x] * (freq_map[x] - 1) // 2
                    elif x < y:
                        count += freq_map[x] * freq_map[y]
        return count

    def numTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        total_triplets = 0

        for num1_val in nums1:
            target_square = num1_val * num1_val
            total_triplets += self.count_pairs_from_array(nums2, target_square)

        for num2_val in nums2:
            target_square = num2_val * num2_val
            total_triplets += self.count_pairs_from_array(nums1, target_square)

        return total_triplets