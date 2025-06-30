class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        n = len(s)
        result = []
        
        def is_valid_part(part_str: str) -> bool:
            if not part_str:
                return False
            if len(part_str) > 1 and part_str[0] == '0':
                return False
            num = int(part_str)
            return 0 <= num <= 255

        def backtrack(index: int, current_parts: list[str]):
            if len(current_parts) == 4:
                if index == n:
                    result.append(".".join(current_parts))
                return

            remaining_parts_count = 4 - len(current_parts)
            if (n - index) < remaining_parts_count or (n - index) > remaining_parts_count * 3:
                return

            for length in range(1, 4):
                if index + length > n:
                    break
                
                part = s[index : index + length]
                
                if is_valid_part(part):
                    current_parts.append(part)
                    backtrack(index + length, current_parts)
                    current_parts.pop()

        backtrack(0, [])
        return result