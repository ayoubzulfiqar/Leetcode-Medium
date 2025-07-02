import collections

class Solution:
    def originalDigits(self, s: str) -> str:
        char_counts = collections.Counter(s)
        digit_counts = [0] * 10

        # Digits with unique identifying characters
        # 'z' in 'zero' (0)
        # 'w' in 'two' (2)
        # 'u' in 'four' (4)
        # 'x' in 'six' (6)
        # 'g' in 'eight' (8)
        digit_counts[0] = char_counts['z']
        digit_counts[2] = char_counts['w']
        digit_counts[4] = char_counts['u']
        digit_counts[6] = char_counts['x']
        digit_counts[8] = char_counts['g']

        # Digits whose identifying character becomes unique after removing the first set
        # 'h' in 'three' (3) but also in 'eight'. So, count(h) - count(8)
        # 'f' in 'five' (5) but also in 'four'. So, count(f) - count(4)
        # 's' in 'seven' (7) but also in 'six'. So, count(s) - count(6)
        digit_counts[3] = char_counts['h'] - digit_counts[8]
        digit_counts[5] = char_counts['f'] - digit_counts[4]
        digit_counts[7] = char_counts['s'] - digit_counts[6]

        # Remaining digits
        # 'o' in 'one' (1) but also in 'zero', 'two', 'four'. So, count(o) - count(0) - count(2) - count(4)
        # 'i' in 'nine' (9) but also in 'five', 'six', 'eight'. So, count(i) - count(5) - count(6) - count(8)
        digit_counts[1] = char_counts['o'] - digit_counts[0] - digit_counts[2] - digit_counts[4]
        digit_counts[9] = char_counts['i'] - digit_counts[5] - digit_counts[6] - digit_counts[8]

        # Construct the result string in ascending order
        result = []
        for i in range(10):
            result.append(str(i) * digit_counts[i])

        return "".join(result)