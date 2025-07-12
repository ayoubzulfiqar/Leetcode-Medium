class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk_bottles = 0
        empty_bottles = 0
        current_full_bottles = numBottles
        current_exchange_rate = numExchange

        while current_full_bottles > 0 or empty_bottles >= current_exchange_rate:
            # Drink all current full bottles
            drunk_bottles += current_full_bottles
            empty_bottles += current_full_bottles
            current_full_bottles = 0

            # Try to make an exchange
            if empty_bottles >= current_exchange_rate:
                empty_bottles -= current_exchange_rate
                current_full_bottles += 1
                current_exchange_rate += 1
            else:
                # Cannot make any more exchanges and no full bottles to drink
                break
        
        return drunk_bottles