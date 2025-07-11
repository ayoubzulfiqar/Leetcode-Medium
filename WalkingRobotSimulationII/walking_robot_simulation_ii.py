class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        
        self.directions = ["East", "North", "West", "South"]
        self.deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.direction_idx = 0
        
    def step(self, num: int) -> None:
        for _ in range(num):
            while True:
                dx, dy = self.deltas[self.direction_idx]
                next_x, next_y = self.x + dx, self.y + dy

                if 0 <= next_x < self.width and 0 <= next_y < self.height:
                    self.x = next_x
                    self.y = next_y
                    break
                else:
                    self.direction_idx = (self.direction_idx + 1) % 4
    
    def getPos(self) -> list[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.directions[self.direction_idx]