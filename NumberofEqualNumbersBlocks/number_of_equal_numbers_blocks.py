def count_equal_blocks(arr):
    if not arr:
        return 0
    
    block_count = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            block_count += 1
    return block_count

example_input = [1, 1, 2, 3, 3, 3, 4]
result = count_equal_blocks(example_input)
print(result)