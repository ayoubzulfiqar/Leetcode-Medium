class Solution:
    def occurrencesOfElement(self, nums: list[int], queries: list[int], x: int) -> list[int]:
        x_indices = []
        for i in range(len(nums)):
            if nums[i] == x:
                x_indices.append(i)

        answer = []
        for q in queries:
            # queries[i] is 1-indexed, so we need (q-1)-th index in x_indices
            if q - 1 < len(x_indices):
                answer.append(x_indices[q - 1])
            else:
                answer.append(-1)
        
        return answer