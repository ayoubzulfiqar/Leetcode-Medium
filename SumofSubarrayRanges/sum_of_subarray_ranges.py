class Solution:
    def sumSubarrayRanges(self, nums: list[int]) -> int:
        n = len(nums)

        # Calculate prev_smaller and next_smaller
        # prev_smaller[i]: index of the previous element strictly smaller than nums[i]. -1 if none.
        # next_smaller[i]: index of the next element smaller than or equal to nums[i]. n if none.
        prev_smaller = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)

        next_smaller = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)

        # Calculate prev_greater and next_greater
        # prev_greater[i]: index of the previous element strictly greater than nums[i]. -1 if none.
        # next_greater[i]: index of the next element greater than or equal to nums[i]. n if none.
        prev_greater = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                prev_greater[i] = stack[-1]
            stack.append(i)

        next_greater = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                next_greater[i] = stack[-1]
            stack.append(i)

        total_min_sum = 0
        for i in range(n):
            # For nums[i] to be the minimum, the subarray must start after prev_smaller[i]
            # and end before next_smaller[i].
            # Number of choices for start index: i - prev_smaller[i]
            # Number of choices for end index: next_smaller[i] - i
            left_bound = prev_smaller[i]
            right_bound = next_smaller[i]
            count = (i - left_bound) * (right_bound - i)
            total_min_sum += nums[i] * count

        total_max_sum = 0
        for i in range(n):
            # For nums[i] to be the maximum, the subarray must start after prev_greater[i]
            # and end before next_greater[i].
            # Number of choices for start index: i - prev_greater[i]
            # Number of choices for end index: next_greater[i] - i
            left_bound = prev_greater[i]
            right_bound = next_greater[i]
            count = (i - left_bound) * (right_bound - i)
            total_max_sum += nums[i] * count

        return total_max_sum - total_min_sum