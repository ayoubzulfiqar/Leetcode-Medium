class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        chosen_elements = set()
        total_sum = 0
        current_num = 1

        while len(chosen_elements) < n:
            complement = k - current_num
            if complement <= 0 or complement not in chosen_elements:
                chosen_elements.add(current_num)
                total_sum += current_num
            current_num += 1
            
        return total_sum