class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for new_asteroid in asteroids:
            collided = False
            while stack and new_asteroid < 0 and stack[-1] > 0:
                top_asteroid = stack[-1]

                if abs(new_asteroid) > abs(top_asteroid):
                    stack.pop()
                elif abs(new_asteroid) == abs(top_asteroid):
                    stack.pop()
                    collided = True
                    break
                else: # abs(new_asteroid) < abs(top_asteroid)
                    collided = True
                    break

            if not collided:
                stack.append(new_asteroid)

        return stack