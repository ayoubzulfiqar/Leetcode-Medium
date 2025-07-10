class Allocator:
    def __init__(self, n: int):
        self.memory = [0] * n
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        current_free_count = 0
        start_index = -1

        for i in range(self.n):
            if self.memory[i] == 0:
                if start_index == -1:
                    start_index = i
                current_free_count += 1
            else:
                current_free_count = 0
                start_index = -1
            
            if current_free_count == size:
                for j in range(start_index, start_index + size):
                    self.memory[j] = mID
                return start_index
        
        return -1

    def freeMemory(self, mID: int) -> int:
        freed_count = 0
        for i in range(self.n):
            if self.memory[i] == mID:
                self.memory[i] = 0
                freed_count += 1
        return freed_count

