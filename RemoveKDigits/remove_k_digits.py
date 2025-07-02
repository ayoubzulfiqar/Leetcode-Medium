class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [] # This will store the digits of the smallest number
        
        for digit in num:
            # While we have removals left (k > 0),
            # and the stack is not empty,
            # and the current digit is smaller than the last digit in the stack:
            # Pop the last digit from the stack. This is a greedy choice
            # to remove a larger digit at a higher place value.
            while k > 0 and stack and digit < stack[-1]:
                stack.pop()
                k -= 1
            
            # Append the current digit to the stack.
            stack.append(digit)
        
        # If k is still greater than 0, it means we haven't removed enough digits.
        # This happens when the remaining digits in the stack are in non-decreasing order
        # (e.g., "12345"). In this case, we must remove the last k digits.
        # We can simply slice the stack to remove the last k elements.
        # If k is larger than len(stack), it will result in an empty stack, which is correct.
        stack = stack[:-k] if k > 0 else stack
        
        # Join the digits in the stack to form the result string.
        res = "".join(stack)
        
        # Remove any leading zeros from the result.
        # For example, "00123" should become "123".
        res = res.lstrip('0')
        
        # If the result string is empty after removing leading zeros (e.g., "0", k=1 -> ""),
        # or if all digits were removed, the result should be "0".
        return res if res else "0"