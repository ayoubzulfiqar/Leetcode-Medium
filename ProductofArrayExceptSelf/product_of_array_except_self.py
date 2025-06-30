class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        answer = [0] * n
        
        # Calculate left products and store them in the answer array
        # answer[i] will contain the product of all elements to the left of nums[i]
        # For the first element, there are no elements to its left, so the product is 1.
        answer[0] = 1
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]
            
        # Calculate right products and combine with left products
        # We use a variable 'right_product' to keep track of the product of elements to the right
        # Initialize right_product to 1 (product of elements to the right of the last element is 1)
        right_product = 1
        for i in range(n - 1, -1, -1):
            # For the current element nums[i], answer[i] already holds the product of elements to its left.
            # Multiply it by the product of elements to its right (right_product).
            answer[i] = answer[i] * right_product
            
            # Update right_product for the next iteration (moving leftwards)
            right_product = right_product * nums[i]
            
        return answer