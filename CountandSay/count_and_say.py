class Solution:
    def _rle(self, s: str) -> str:
        if not s:
            return ""

        result_parts = []
        count = 1
        current_char = s[0]

        for i in range(1, len(s)):
            if s[i] == current_char:
                count += 1
            else:
                result_parts.append(str(count))
                result_parts.append(current_char)
                current_char = s[i]
                count = 1
        
        result_parts.append(str(count))
        result_parts.append(current_char)

        return "".join(result_parts)

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        current_string = "1"
        for _ in range(2, n + 1):
            current_string = self._rle(current_string)
        
        return current_string