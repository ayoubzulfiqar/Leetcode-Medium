class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > (3 * (2**(n - 1))):
            return ""

        self.count = 0
        self.result = ""

        def backtrack(current_str):
            if self.result:
                return

            if len(current_str) == n:
                self.count += 1
                if self.count == k:
                    self.result = current_str
                return

            last_char = ''
            if current_str:
                last_char = current_str[-1]

            for char_code in range(ord('a'), ord('c') + 1):
                char = chr(char_code)
                if char != last_char:
                    backtrack(current_str + char)
                    if self.result:
                        return

        backtrack("")
        return self.result