class Solution:
    def _remove_and_score(self, s_orig, char1, char2, points):
        score = 0
        stack = []
        for char in s_orig:
            if stack and char == char2 and stack[-1] == char1:
                stack.pop()
                score += points
            else:
                stack.append(char)
        
        remaining_s = "".join(stack)
        return score, remaining_s

    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_score = 0

        if x >= y:
            first_pair_char1, first_pair_char2 = 'a', 'b'
            first_pair_points = x
            second_pair_char1, second_pair_char2 = 'b', 'a'
            second_pair_points = y
        else:
            first_pair_char1, first_pair_char2 = 'b', 'a'
            first_pair_points = y
            second_pair_char1, second_pair_char2 = 'a', 'b'
            second_pair_points = x
        
        score_first_pass, remaining_s_after_first_pass = self._remove_and_score(s, first_pair_char1, first_pair_char2, first_pair_points)
        total_score += score_first_pass

        score_second_pass, _ = self._remove_and_score(remaining_s_after_first_pass, second_pair_char1, second_pair_char2, second_pair_points)
        total_score += score_second_pass

        return total_score