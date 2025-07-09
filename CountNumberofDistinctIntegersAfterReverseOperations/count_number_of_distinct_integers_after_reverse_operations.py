class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        distinct_numbers = set()

        def reverse_digits(n: int) -> int:
            # Convert integer to string, reverse the string, and convert back to integer.
            # This handles cases like 10 becoming 1 (01 as string becomes 1 as int).
            return int(str(n)[::-1])

        for num in nums:
            distinct_numbers.add(num)
            reversed_num = reverse_digits(num)
            distinct_numbers.add(reversed_num)

        return len(distinct_numbers)