class Solution:
    def canWin(self, s: str) -> bool:
        memo = {}

        def can_win_recursive(current_s: str) -> bool:
            if current_s in memo:
                return memo[current_s]

            for i in range(len(current_s) - 1):
                if current_s[i:i+2] == "++":
                    next_s_list = list(current_s)
                    next_s_list[i] = '-'
                    next_s_list[i+1] = '-'
                    next_s = "".join(next_s_list)

                    if not can_win_recursive(next_s):
                        memo[current_s] = True
                        return True
            
            memo[current_s] = False
            return False

        return can_win_recursive(s)