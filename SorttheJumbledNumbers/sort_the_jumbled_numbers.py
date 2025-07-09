class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        def map_number(num: int) -> int:
            s_num = str(num)
            mapped_s_digits = []
            for char_digit in s_num:
                digit = int(char_digit)
                mapped_digit = mapping[digit]
                mapped_s_digits.append(str(mapped_digit))
            
            return int("".join(mapped_s_digits))

        nums.sort(key=map_number)
        
        return nums