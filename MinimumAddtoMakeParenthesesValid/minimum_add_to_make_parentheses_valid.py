class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_balance = 0
        insertions = 0

        for char in s:
            if char == '(':
                open_balance += 1
            else:  # char == ')'
                if open_balance > 0:
                    open_balance -= 1
                else:
                    insertions += 1
        
        insertions += open_balance
        
        return insertions