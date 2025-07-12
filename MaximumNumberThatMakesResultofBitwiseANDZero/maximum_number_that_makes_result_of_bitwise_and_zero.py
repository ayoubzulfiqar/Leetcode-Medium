def max_number_bitwise_and_zero(n: int) -> int:
    if n == 0:
        return 0
    
    num_bits = n.bit_length()
    mask = (1 << num_bits) - 1
    return mask ^ n