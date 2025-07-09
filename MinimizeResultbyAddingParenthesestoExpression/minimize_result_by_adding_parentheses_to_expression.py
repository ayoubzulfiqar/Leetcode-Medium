class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus_idx = expression.find('+')
        n = len(expression)

        min_val = float('inf')
        best_expr = ""

        for i in range(plus_idx):
            prefix_str = expression[0:i]
            left_in_paren_str = expression[i:plus_idx]
            
            prefix_val = int(prefix_str) if prefix_str else 1

            for j in range(plus_idx + 1, n):
                right_in_paren_str = expression[plus_idx+1:j+1]
                suffix_str = expression[j+1:n]
                
                suffix_val = int(suffix_str) if suffix_str else 1

                current_sum = int(left_in_paren_str) + int(right_in_paren_str)
                current_product = prefix_val * current_sum * suffix_val

                if current_product < min_val:
                    min_val = current_product
                    best_expr = prefix_str + '(' + left_in_paren_str + '+' + right_in_paren_str + ')' + suffix_str
        
        return best_expr