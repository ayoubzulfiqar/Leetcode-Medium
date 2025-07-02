class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total_sum = sum(matchsticks)

        if total_sum % 4 != 0:
            return False
        
        target_side_length = total_sum // 4

        for stick in matchsticks:
            if stick > target_side_length:
                return False

        matchsticks.sort(reverse=True)

        sides = [0] * 4

        def backtrack(index):
            if index == len(matchsticks):
                return True

            current_stick = matchsticks[index]

            for i in range(4):
                if i > 0 and sides[i] == sides[i-1]:
                    continue

                if sides[i] + current_stick <= target_side_length:
                    sides[i] += current_stick
                    if backtrack(index + 1):
                        return True
                    sides[i] -= current_stick

            return False

        return backtrack(0)