from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        row_map = defaultdict(set)
        for r, c in reservedSeats:
            row_map[r].add(c)

        total_groups = 2 * n

        for row_num, reserved_set in row_map.items():
            total_groups -= 2 

            can_place_left = True
            for seat in [2, 3, 4, 5]:
                if seat in reserved_set:
                    can_place_left = False
                    break
            
            can_place_middle = True
            for seat in [4, 5, 6, 7]:
                if seat in reserved_set:
                    can_place_middle = False
                    break
            
            can_place_right = True
            for seat in [6, 7, 8, 9]:
                if seat in reserved_set:
                    can_place_right = False
                    break

            groups_in_this_row = 0
            if can_place_left and can_place_right:
                groups_in_this_row = 2
            elif can_place_left or can_place_middle or can_place_right:
                groups_in_this_row = 1
            
            total_groups += groups_in_this_row
        
        return total_groups