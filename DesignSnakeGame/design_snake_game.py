import collections

class SnakeGame:

    def __init__(self, width: int, height: int, food: list[list[int]]):
        self.width = width
        self.height = height
        self.food_list = food
        self.food_idx = 0
        self.score = 0

        self.snake_body = collections.deque([(0, 0)])
        self.snake_set = {(0, 0)}

        self.directions = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }

    def move(self, direction: str) -> int:
        curr_head_r, curr_head_c = self.snake_body[0]
        dr, dc = self.directions[direction]
        new_head_r, new_head_c = curr_head_r + dr, curr_head_c + dc

        if not (0 <= new_head_r < self.height and 0 <= new_head_c < self.width):
            return -1

        is_food_eaten = False
        if self.food_idx < len(self.food_list) and \
           new_head_r == self.food_list[self.food_idx][0] and \
           new_head_c == self.food_list[self.food_idx][1]:
            is_food_eaten = True

        tail_r, tail_c = self.snake_body[-1]

        if not is_food_eaten:
            self.snake_body.pop()
            self.snake_set.remove((tail_r, tail_c))
        else:
            self.score += 1
            self.food_idx += 1

        if (new_head_r, new_head_c) in self.snake_set:
            return -1

        self.snake_body.appendleft((new_head_r, new_head_c))
        self.snake_set.add((new_head_r, new_head_c))

        return self.score