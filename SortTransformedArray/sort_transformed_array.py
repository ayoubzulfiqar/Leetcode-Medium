class Solution:
    def sortTransformedArray(self, nums: list[int], a: int, b: int, c: int) -> list[int]:
        n = len(nums)
        if n == 0:
            return []

        def calculate_transformed_value(x: int) -> int:
            return a * x * x + b * x + c

        result = [0] * n
        left, right = 0, n - 1

        if a >= 0:
            k = n - 1
            while left <= right:
                val_left = calculate_transformed_value(nums[left])
                val_right = calculate_transformed_value(nums[right])

                if val_left > val_right:
                    result[k] = val_left
                    left += 1
                else:
                    result[k] = val_right
                    right -= 1
                k -= 1
        else:
            k = 0
            while left <= right:
                val_left = calculate_transformed_value(nums[left])
                val_right = calculate_transformed_value(nums[right])

                if val_left < val_right:
                    result[k] = val_left
                    left += 1
                else:
                    result[k] = val_right
                    right -= 1
                k += 1
        
        return result