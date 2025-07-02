import collections

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        allowed_map = collections.defaultdict(list)
        for pattern in allowed:
            bottom_left, bottom_right, top = pattern[0], pattern[1], pattern[2]
            allowed_map[(bottom_left, bottom_right)].append(top)

        memo = {}

        def solve(current_row_chars: tuple) -> bool:
            if len(current_row_chars) == 1:
                return True

            if current_row_chars in memo:
                return memo[current_row_chars]

            possible_next_rows = []

            def generate_next_row_combinations(current_index: int, built_next_row: list):
                if current_index == len(current_row_chars) - 1:
                    possible_next_rows.append(tuple(built_next_row))
                    return

                left_char = current_row_chars[current_index]
                right_char = current_row_chars[current_index + 1]

                if (left_char, right_char) not in allowed_map:
                    return

                for top_char in allowed_map[(left_char, right_char)]:
                    built_next_row.append(top_char)
                    generate_next_row_combinations(current_index + 1, built_next_row)
                    built_next_row.pop()

            generate_next_row_combinations(0, [])

            for next_row_tuple in possible_next_rows:
                if solve(next_row_tuple):
                    memo[current_row_chars] = True
                    return True

            memo[current_row_chars] = False
            return False

        return solve(tuple(bottom))