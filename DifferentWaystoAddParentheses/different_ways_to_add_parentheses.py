class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        memo = {}

        def compute(sub_expr: str) -> list[int]:
            if sub_expr in memo:
                return memo[sub_expr]

            results = []
            is_number = True
            for i, char in enumerate(sub_expr):
                if char in '+-*':
                    is_number = False
                    
                    left_part = sub_expr[:i]
                    right_part = sub_expr[i+1:]

                    left_results = compute(left_part)
                    right_results = compute(right_part)

                    for l_val in left_results:
                        for r_val in right_results:
                            if char == '+':
                                results.append(l_val + r_val)
                            elif char == '-':
                                results.append(l_val - r_val)
                            elif char == '*':
                                results.append(l_val * r_val)
            
            if is_number:
                results.append(int(sub_expr))
            
            memo[sub_expr] = results
            return results

        return compute(expression)