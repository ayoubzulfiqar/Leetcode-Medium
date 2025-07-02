class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            # Email address
            s = s.lower()
            parts = s.split('@')
            name = parts[0]
            domain = parts[1]

            masked_name = name[0] + "*****" + name[-1]
            return masked_name + "@" + domain
        else:
            # Phone number
            digits_only = ""
            for char in s:
                if char.isdigit():
                    digits_only += char

            n = len(digits_only)
            last_four = digits_only[-4:]

            if n == 10:
                return "***-***-" + last_four
            elif n == 11:
                return "+*-***-***-" + last_four
            elif n == 12:
                return "+**-***-***-" + last_four
            elif n == 13:
                return "+***-***-***-" + last_four

```