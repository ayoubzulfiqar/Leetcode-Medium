class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> list[int]:
        powerful_integers = set()

        val_x = 1
        while val_x <= bound:
            val_y = 1
            while val_x + val_y <= bound:
                powerful_integers.add(val_x + val_y)
                
                if y == 1:
                    break
                val_y *= y
            
            if x == 1:
                break
            val_x *= x
        
        return list(powerful_integers)