class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def backtrack(index: int, prev_val: int, count: int) -> bool:
            if index == n:
                return count >= 2

            for i in range(index, n):
                current_str = s[index : i + 1]
                current_val = int(current_str)

                if current_val == prev_val - 1:
                    if backtrack(i + 1, current_val, count + 1):
                        return True
            
            return False

        for i in range(n - 1):
            first_str = s[0 : i + 1]
            first_val = int(first_str)

            if backtrack(i + 1, first_val, 1):
                return True

        return False