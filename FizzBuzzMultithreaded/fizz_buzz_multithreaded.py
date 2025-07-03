import threading
from typing import Callable

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.current_number = 1
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)

    def fizz(self, printFizz: Callable[[], None]) -> None:
        while True:
            with self.cond:
                while self.current_number <= self.n and \
                      (self.current_number % 3 != 0 or self.current_number % 5 == 0):
                    self.cond.wait()
                
                if self.current_number > self.n:
                    break
                
                printFizz()
                self.current_number += 1
                self.cond.notify_all()

    def buzz(self, printBuzz: Callable[[], None]) -> None:
        while True:
            with self.cond:
                while self.current_number <= self.n and \
                      (self.current_number % 5 != 0 or self.current_number % 3 == 0):
                    self.cond.wait()

                if self.current_number > self.n:
                    break

                printBuzz()
                self.current_number += 1
                self.cond.notify_all()

    def fizzbuzz(self, printFizzBuzz: Callable[[], None]) -> None:
        while True:
            with self.cond:
                while self.current_number <= self.n and \
                      self.current_number % 15 != 0:
                    self.cond.wait()
                
                if self.current_number > self.n:
                    break

                printFizzBuzz()
                self.current_number += 1
                self.cond.notify_all()

    def number(self, printNumber: Callable[[int], None]) -> None:
        while True:
            with self.cond:
                while self.current_number <= self.n and \
                      (self.current_number % 3 == 0 or self.current_number % 5 == 0):
                    self.cond.wait()
                
                if self.current_number > self.n:
                    break

                printNumber(self.current_number)
                self.current_number += 1
                self.cond.notify_all()