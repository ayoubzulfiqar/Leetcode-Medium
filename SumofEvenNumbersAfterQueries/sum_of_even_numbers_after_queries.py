class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        current_even_sum = 0
        for num in nums:
            if num % 2 == 0:
                current_even_sum += num

        answer = []
        for val, index in queries:
            # If the old number at index was even, subtract it from the sum
            if nums[index] % 2 == 0:
                current_even_sum -= nums[index]
            
            # Update the number
            nums[index] += val
            
            # If the new number at index is even, add it to the sum
            if nums[index] % 2 == 0:
                current_even_sum += nums[index]
            
            answer.append(current_even_sum)
            
        return answer