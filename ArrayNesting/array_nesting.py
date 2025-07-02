class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        n = len(nums)
        visited = [False] * n
        max_length = 0

        for i in range(n):
            if not visited[i]:
                current_length = 0
                current_element = i
                while not visited[current_element]:
                    visited[current_element] = True
                    current_element = nums[current_element]
                    current_length += 1
                max_length = max(max_length, current_length)
        
        return max_length