class Solution:
    def addNegabinary(self, arr1: list[int], arr2: list[int]) -> list[int]:
        arr1_rev = arr1[::-1]
        arr2_rev = arr2[::-1]

        n = max(len(arr1_rev), len(arr2_rev))

        result = []
        carry = 0

        for i in range(n + 2):
            val1 = arr1_rev[i] if i < len(arr1_rev) else 0
            val2 = arr2_rev[i] if i < len(arr2_rev) else 0

            current_sum = val1 + val2 + carry

            if current_sum == 0:
                result.append(0)
                carry = 0
            elif current_sum == 1:
                result.append(1)
                carry = 0
            elif current_sum == 2:
                result.append(0)
                carry = -1
            elif current_sum == 3:
                result.append(1)
                carry = -1
            elif current_sum == -1:
                result.append(1)
                carry = 1
            
        result.reverse()

        while len(result) > 1 and result[0] == 0:
            result.pop(0)
            
        return result