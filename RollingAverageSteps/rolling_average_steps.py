def calculate_rolling_average(data, window_size):
    if not data or window_size <= 0 or window_size > len(data):
        return []

    averages = []
    current_sum = sum(data[0:window_size])
    averages.append(current_sum / window_size)

    for i in range(window_size, len(data)):
        current_sum = current_sum - data[i - window_size] + data[i]
        averages.append(current_sum / window_size)

    return averages

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 3, [2.0, 3.0, 4.0]),
        ([10, 20, 30, 40, 50, 60], 4, [25.0, 35.0, 45.0]),
        ([1, 2], 3, []),
        ([], 2, []),
        ([1, 2, 3], 1, [1.0, 2.0, 3.0]),
        ([1, 2, 3], 0, []),
        ([5], 1, [5.0]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, [3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
    ]

    for data, window_size, expected in test_cases:
        result = calculate_rolling_average(data, window_size)
        assert result == expected, f"Test failed for data={data}, window_size={window_size}. Expected {expected}, got {result}"