def solve_nim(piles):
    nim_sum = 0
    for pile_size in piles:
        nim_sum ^= pile_size
    return nim_sum != 0