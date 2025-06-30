class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result_parts = []
        
        if (numerator < 0) != (denominator < 0):
            result_parts.append("-")
        
        num = abs(numerator)
        den = abs(denominator)
        
        result_parts.append(str(num // den))
        
        remainder = num % den
        
        if remainder == 0:
            return "".join(result_parts)
            
        result_parts.append(".")
        
        remainder_map = {} 
        decimal_digits = []
        
        current_decimal_index = 0
        while remainder != 0:
            if remainder in remainder_map:
                cycle_start_index = remainder_map[remainder]
                
                decimal_digits.insert(cycle_start_index, "(")
                decimal_digits.append(")")
                break
            
            remainder_map[remainder] = current_decimal_index
            
            remainder *= 10
            digit = remainder // den
            decimal_digits.append(str(digit))
            
            remainder %= den
            current_decimal_index += 1
            
        result_parts.extend(decimal_digits)
        
        return "".join(result_parts)