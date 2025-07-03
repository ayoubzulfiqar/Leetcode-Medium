class Solution:
    def is_prime(self, num: int) -> bool:
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2
        return True

    def primePalindrome(self, n: int) -> int:
        if n <= 2:
            return 2
        if n == 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if 8 <= n <= 11:
            return 11

        for i in range(1, 20000):
            s = str(i)
            p_str = s + s[:-1][::-1]
            p_num = int(p_str)

            if p_num >= n and self.is_prime(p_num):
                return p_num
        
        return -1