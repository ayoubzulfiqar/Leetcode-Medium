import threading
from typing import Callable

class ZeroEvenOdd:
    def __init__(self, n: int):
        self.n = n
        self.current_num = 1
        self.state = 0  # 0: zero's turn, 1: odd's turn, 2: even's turn
        self.condition = threading.Condition()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            with self.condition:
                while self.state != 0:
                    self.condition.wait()
                
                printNumber(0)
                
                if self.current_num % 2 == 1: # Next number to print is odd
                    self.state = 1
                else: # Next number to print is even
                    self.state = 2
                
                self.condition.notify_all()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.condition:
                # Wait if it's not even's turn OR if all numbers have been printed
                while self.state != 2 and self.current_num <= self.n:
                    self.condition.wait()
                
                # If all numbers have been printed, exit this thread
                if self.current_num > self.n:
                    break
                
                printNumber(self.current_num)
                self.current_num += 1
                self.state = 0 # It's zero's turn next
                self.condition.notify_all()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.condition:
                # Wait if it's not odd's turn OR if all numbers have been printed
                while self.state != 1 and self.current_num <= self.n:
                    self.condition.wait()
                
                # If all numbers have been printed, exit this thread
                if self.current_num > self.n:
                    break
                
                printNumber(self.current_num)
                self.current_num += 1
                self.state = 0 # It's zero's turn next
                self.condition.notify_all()