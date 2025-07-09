class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bits_actual = [0] * size
        self.count_ones = 0
        self.is_flipped = False

    def fix(self, idx: int) -> None:
        current_actual_bit = self.bits_actual[idx]
        
        if not self.is_flipped:
            # If not flipped, to make effective bit 1, actual bit must be 1.
            if current_actual_bit == 0:
                self.bits_actual[idx] = 1
                self.count_ones += 1
        else:
            # If flipped, to make effective bit 1, actual bit must be 0.
            if current_actual_bit == 1:
                self.bits_actual[idx] = 0
                self.count_ones += 1

    def unfix(self, idx: int) -> None:
        current_actual_bit = self.bits_actual[idx]

        if not self.is_flipped:
            # If not flipped, to make effective bit 0, actual bit must be 0.
            if current_actual_bit == 1:
                self.bits_actual[idx] = 0
                self.count_ones -= 1
        else:
            # If flipped, to make effective bit 0, actual bit must be 1.
            if current_actual_bit == 0:
                self.bits_actual[idx] = 1
                self.count_ones -= 1

    def flip(self) -> None:
        self.is_flipped = not self.is_flipped
        self.count_ones = self.size - self.count_ones

    def all(self) -> bool:
        return self.count_ones == self.size

    def one(self) -> bool:
        return self.count_ones > 0

    def count(self) -> int:
        return self.count_ones

    def toString(self) -> str:
        if not self.is_flipped:
            return "".join(map(str, self.bits_actual))
        else:
            return "".join(map(lambda x: str(1 - x), self.bits_actual))

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_5 = obj.all()
# param_6 = obj.one()
# param_7 = obj.count()
# param_8 = obj.toString()