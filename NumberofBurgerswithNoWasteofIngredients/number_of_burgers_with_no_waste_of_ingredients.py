class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> list[int]:
        numerator_for_jumbo = tomatoSlices - 2 * cheeseSlices

        if numerator_for_jumbo < 0 or numerator_for_jumbo % 2 != 0:
            return []

        jumbo_burgers = numerator_for_jumbo // 2

        small_burgers = cheeseSlices - jumbo_burgers

        if small_burgers < 0:
            return []

        return [jumbo_burgers, small_burgers]