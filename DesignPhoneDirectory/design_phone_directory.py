class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.available_numbers = set(range(maxNumbers))
        self.used_numbers = set()

    def get(self) -> int:
        if not self.available_numbers:
            return -1
        
        num = self.available_numbers.pop()
        self.used_numbers.add(num)
        return num

    def check(self, number: int) -> bool:
        return number in self.available_numbers

    def release(self, number: int) -> None:
        if number in self.used_numbers:
            self.used_numbers.remove(number)
            self.available_numbers.add(number)