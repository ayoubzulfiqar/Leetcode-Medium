class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        count_a = a
        count_b = b

        while count_a > 0 or count_b > 0:
            # Determine if 'a' can be added without forming 'aaa'
            # This is true if count_a > 0 AND (the string is too short to have 'aa' or it doesn't end in 'aa')
            can_add_a_now = (count_a > 0) and (len(res) < 2 or res[-1] != 'a' or res[-2] != 'a')
            
            # Determine if 'b' can be added without forming 'bbb'
            # This is true if count_b