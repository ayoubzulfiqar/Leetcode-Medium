class Solution:
    def mostCompetitive(self, nums: list[int], k: int) -> list[int]:
        stack = []
        n = len(nums)

        for i, num in enumerate(nums):
            # Pop elements from stack if:
            # 1. The stack is not empty.
            # 2. The current number `num` is smaller than the top of the stack `stack[-1]`.
            # 3. We still have enough elements remaining in `nums` (from current index `i` to the end)
            #    to form a subsequence of length `k` even after popping `stack[-1]`.
            #    `len(stack) - 1` is the size of the stack after popping.
            #    `n - i` is the number of elements available from `nums[i]` onwards.
            #    Their sum must be at least `k`.
            while stack and num < stack[-1] and (len(stack) - 1) + (n - i) >= k:
                stack.pop()

            # Append the current number `num` if the stack has less than `k` elements.
            # If the stack already has `k` elements and no element was popped,
            # it means `num` was not competitive enough or popping would make it impossible to reach `k` length,
            # so we do not append `num` in that case.
            if len(stack) < k:
                stack.append(num)
        
        return stack