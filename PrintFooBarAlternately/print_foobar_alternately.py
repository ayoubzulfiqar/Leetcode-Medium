import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_sem = threading.Semaphore(1)
        self.bar_sem = threading.Semaphore(0)

    def foo(self) -> None:
        for i in range(self.n):
            self.foo_sem.acquire()
            print("foo", end='')
            self.bar_sem.release()

    def bar(self) -> None:
        for i in range(self.n):
            self.bar_sem.acquire()
            print("bar", end='')
            self.foo_sem.release()