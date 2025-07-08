def is_numerically_balanced(num):
    s_num = str(num)
    counts = [0] * 10

    for char_digit in s_num:
        digit = int(char_digit)
        counts[digit] += 1

    for digit in range(10):
        if counts[digit] > 0:
            if counts[digit] != digit:
                return False
        if digit == 0 and counts[0] > 0:
            return False
    return True

def next_greater_numerically_balanced_number(n: int) -> int:
    num = n + 1
    while True:
        if is_numerically_balanced(num):
            return num
        num += 1