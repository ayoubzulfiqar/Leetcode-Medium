def sum_consecutive_subarrays(arr):
    total_sum = 0
    n = len(arr)
    for i in range(n):
        total_sum += arr[i] * (i + 1) * (n - i)
    return total_sum

if __name__ == "__main__":
    # Example usage to demonstrate the function's completeness.
    # The problem does not specify input/output methods for a script,
    # so an internal test case is used.
    test_array = [1, 2, 3]
    result = sum_consecutive_subarrays(test_array)
    # For [1, 2, 3], the expected sum is 20.
    # (1) + (2) + (3) + (1+2) + (2+3) + (1+2+3) = 1 + 2 + 3 + 3 + 5 + 6 = 20
    pass