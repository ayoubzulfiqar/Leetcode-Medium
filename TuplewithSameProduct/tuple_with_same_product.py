import collections

class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        product_counts = collections.defaultdict(int)
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_counts[product] += 1
        
        total_tuples = 0
        
        for count_for_product in product_counts.values():
            if count_for_product >= 2:
                num_combinations = count_for_product * (count_for_product - 1) // 2
                total_tuples += num_combinations * 8
                
        return total_tuples