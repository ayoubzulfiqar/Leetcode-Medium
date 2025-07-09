class Solution:
    def canDestroy(self, mass: int, asteroids: list[int]) -> bool:
        asteroids.sort()
        current_mass = mass
        for asteroid_mass in asteroids:
            if current_mass >= asteroid_mass:
                current_mass += asteroid_mass
            else:
                return False
        return True