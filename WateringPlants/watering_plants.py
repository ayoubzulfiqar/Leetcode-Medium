class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        steps = 0
        current_water = capacity
        current_pos = -1

        n = len(plants)

        for i in range(n):
            steps += (i - current_pos)
            current_pos = i

            current_water -= plants[i]

            if i < n - 1:
                if current_water < plants[i + 1]:
                    steps += (i - (-1))
                    current_water = capacity
                    current_pos = -1
        
        return steps