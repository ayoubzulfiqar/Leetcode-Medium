class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder_map = {0: -1}
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            remainder = current_sum % k

            if remainder in remainder_map:
                prev_index = remainder_map[remainder]
                if i - prev_index >= 2:
                    return True
            else:
                remainder_map[remainder] = i
        
        return False