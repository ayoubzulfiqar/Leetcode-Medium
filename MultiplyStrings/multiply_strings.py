class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n1 = len(num1)
        n2 = len(num2)
        
        res = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])

                product = digit1 * digit2

                pos1 = i + j + 1
                pos2 = i + j     

                current_sum = product + res[pos1]

                res[pos1] = current_sum % 10
                res[pos2] += current_sum // 10
        
        k = 0
        while k < len(res) - 1 and res[k] == 0:
            k += 1
        
        return "".join(map(str, res[k:]))