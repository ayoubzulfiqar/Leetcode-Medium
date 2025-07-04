class CustomStack:
    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        return self.stack.pop()

    def inc(self, k: int, val: int) -> None:
        limit = min(k, len(self.stack))
        for i in range(limit):
            self.stack[i] += val