import math

class Solution:
    def maxEnergyBoost(self, energyDrinkA: list[int], energyDrinkB: list[int]) -> int:
        n = len(energyDrinkA)

        dp_a = energyDrinkA[0]
        dp_b = energyDrinkB[0]
        dp_cleanse = -math.inf 

        for i in range(1, n):
            next_dp_a = max(dp_a, dp_cleanse) + energyDrinkA[i]
            next_dp_b = max(dp_b, dp_cleanse) + energyDrinkB[i]
            next_dp_cleanse = max(dp_a, dp_b)

            dp_a = next_dp_a
            dp_b = next_dp_b
            dp_cleanse = next_dp_cleanse
        
        return max(dp_a, dp_b, dp_cleanse)