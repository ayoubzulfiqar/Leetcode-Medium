import functools

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums_str = [str(num) for num in nums]

        def compare(s1, s2):
            # If s1 + s2 forms a larger number than s2 + s1,
            # then s1 should come before s2 in the final string.
            # In terms of sorting, this means s1 is "greater" than s2
            # in our custom ordering.
            if s1 + s2 > s2 + s1:
                return 1  # s1 is 'greater' than s2
            elif s1 + s2 < s2 + s1:
                return -1 # s1 is 'less' than s2
            else:
                return 0  # s1 is 'equal' to s2

        # Sort the list of strings using the custom comparison logic.
        # functools.cmp_to_key converts a traditional comparison function
        # (which returns -1, 0, or 1) into a key function suitable for `sorted()`.
        # We sort in reverse order because our `compare` function defines
        # "greater than" such that the desired elements come first.
        sorted_nums_str = sorted(nums_str, key=functools.cmp_to_key(compare), reverse=True)

        # Handle the edge case where the result might be "00", "000", etc.
        # If the largest number starts with '0' (and is not just "0"), it means
        # all numbers were zeros, so the result should be "0".
        if sorted_nums_str and sorted_nums_str[0] == '0':
            return "0"

        return "".join(sorted_nums_str)