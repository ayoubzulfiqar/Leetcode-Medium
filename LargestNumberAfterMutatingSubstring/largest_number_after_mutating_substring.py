class Solution:
    def largestNumber(self, num: str, change: list[int]) -> str:
        num_list = list(num)
        n = len(num_list)
        
        mutation_started = False
        
        for i in range(n):
            digit = int(num_list[i])
            mapped_digit = change[digit]
            
            if mutation_started:
                if mapped_digit >= digit:
                    num_list[i] = str(mapped_digit)
                else:
                    break 
            else:
                if mapped_digit > digit:
                    num_list[i] = str(mapped_digit)
                    mutation_started = True
                
        return "".join(num_list)