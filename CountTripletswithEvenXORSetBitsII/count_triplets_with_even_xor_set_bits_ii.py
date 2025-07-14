def solve(nums):
    even_parity_count = 0
    odd_parity_count = 0

    for num in nums:
        popcount = bin(num).count('1')
        
        if popcount % 2 == 0:
            even_parity_count += 1
        else:
            odd_parity_count += 1

    E = even_parity_count
    O = odd_parity_count

    total_triplets = 0

    if E >= 3:
        total_triplets += (E * (E - 1) * (E - 2)) // 6

    if E >= 1 and O >= 2:
        total_triplets += E * (O * (O - 1) // 2)
        
    return total_triplets