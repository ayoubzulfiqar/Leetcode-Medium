class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        target_max_xor_value = (1 << maximumBit) - 1

        current_xor_total = 0
        for num in nums:
            current_xor_total ^= num

        answer = []

        for i in range(len(nums) - 1, -1, -1):
            k = current_xor_total ^ target_max_xor_value
            answer.append(k)
            current_xor_total ^= nums[i]
        
        return answer[::-1]