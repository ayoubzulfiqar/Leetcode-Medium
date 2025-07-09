class Solution:
    def wateringPlants(self, plants: list[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        refills = 0
        alice_current_water = capacityA
        bob_current_water = capacityB
        
        left = 0
        right = n - 1
        
        while left <= right:
            if left == right:
                # Alice and Bob meet at the same plant
                # The one with more water waters it. If equal, Alice waters.
                if alice_current_water >= bob_current_water:
                    if alice_current_water < plants[left]:
                        refills += 1
                        alice_current_water = capacityA
                    alice_current_water -= plants[left]
                else: # Bob has more water
                    if bob_current_water < plants[right]:
                        refills += 1
                        bob_current_water = capacityB
                    bob_current_water -= plants[right]
                break # All plants watered, exit loop
            else:
                # Alice waters plant at `left`
                if alice_current_water < plants[left]:
                    refills += 1
                    alice_current_water = capacityA
                alice_current_water -= plants[left]
                left += 1
                
                # Bob waters plant at `right`
                if bob_current_water < plants[right]:
                    refills += 1
                    bob_current_water = capacityB
                bob_current_water -= plants[right]
                right -= 1
                
        return refills