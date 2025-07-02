class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse_complex(s: str):
            parts = s.split('+')
            real = int(parts[0])
            imaginary = int(parts[1][:-1])
            return real, imaginary

        a, b = parse_complex(num1)
        c, d = parse_complex(num2)

        new_real = a * c - b * d
        new_imaginary = a * d + b * c

        return f"{new_real}+{new_imaginary}i"