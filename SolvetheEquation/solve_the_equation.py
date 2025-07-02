import re

class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse_side(s: str):
            coeff_x = 0
            constant = 0
            
            # Regex to find terms:
            # [+-]?  -> optional sign at the beginning of a term
            # (\d*)x -> optional digits followed by 'x' (e.g., 'x', '2x', '-x', '-2x')
            # |      -> OR
            # [+-]?\d+ -> optional sign followed by one or more digits (e.g., '5', '-3')
            # re.findall returns a list of all non-overlapping matches.
            terms = re.findall(r"([+-]?\d*x|[+-]?\d+)", s)

            for term in terms:
                if 'x' in term:
                    if term == 'x' or term == '+x':
                        coeff_val = 1
                    elif term == '-x':
                        coeff_val = -1
                    else: # e.g., "2x", "-2x", "10x"
                        coeff_val = int(term[:-1])
                    coeff_x += coeff_val
                else: # Constant term
                    constant += int(term)
            return (coeff_x, constant)

        lhs_str, rhs_str = equation.split('=')

        lhs_coeff_x, lhs_const = parse_side(lhs_str)
        rhs_coeff_x, rhs_const = parse_side(rhs_str)

        # Rearrange the equation to the form: total_coeff_x * x = total_const
        # (lhs_coeff_x - rhs_coeff_x) * x = (rhs_const - lhs_const)
        total_coeff_x = lhs_coeff_x - rhs_coeff_x
        total_const = rhs_const - lhs_const

        if total_coeff_x == 0:
            if total_const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            # The problem guarantees that if there is a single solution, it will be an integer.
            x_value = total_const // total_coeff_x
            return f"x={x_value}"