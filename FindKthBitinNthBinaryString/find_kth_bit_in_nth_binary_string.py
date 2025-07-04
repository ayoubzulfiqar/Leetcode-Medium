def findKthBit(n: int, k: int) -> str:
    if n == 1:
        return "0"

    length_sn_minus_1 = (1 << (n - 1)) - 1

    if k <= length_sn_minus_1:
        return findKthBit(n - 1, k)
    elif k == length_sn_minus_1 + 1:
        return "1"
    else:
        k_prime = k - (length_sn_minus_1 + 1)
        
        original_pos_in_sn_minus_1 = length_sn_minus_1 - k_prime + 1

        bit_from_sn_minus_1 = findKthBit(n - 1, original_pos_in_sn_minus_1)

        return "1" if bit_from_sn_minus_1 == "0" else "0"