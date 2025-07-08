class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True

        sum_all_numbers = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if sum_all_numbers < desiredTotal:
            return False

        memo = {}

        def can_win_recursive(current_mask: int, current_total: int) -> bool:
            if current_total >= desiredTotal:
                return False

            if current_mask in memo:
                return memo[current_mask]

            for i in range(1, maxChoosableInteger + 1):
                if not (current_mask & (1 << (i - 1))):
                    if current_total + i >= desiredTotal:
                        memo[current_mask] = True
                        return True

                    if not can_win_recursive(current_mask | (1 << (i - 1)), current_total + i):
                        memo[current_mask] = True
                        return True

            memo[current_mask] = False
            return False

        return can_win_recursive(0, 0)