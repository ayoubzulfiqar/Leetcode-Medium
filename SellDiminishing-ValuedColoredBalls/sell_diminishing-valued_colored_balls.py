class Solution:
    def maxProfit(self, inventory: list[int], orders: int) -> int:
        MOD = 10**9 + 7
        MOD_INV_2 = pow(2, MOD - 2, MOD) # Modular inverse of 2 for arithmetic series sum

        # Helper function to calculate sum of an arithmetic series
        # Sum = count * (start + end) / 2
        def sum_arithmetic_series(start, end, count):
            if count == 0:
                return 0
            s = (start % MOD + end % MOD) % MOD
            c = count % MOD
            return (c * s % MOD * MOD_INV_2) % MOD

        inventory.sort(reverse=True)
        n = len(inventory)
        total_value = 0
        
        current_max_val_idx = 0
        
        while orders > 0 and current_max_val_idx < n:
            current_val = inventory[current_max_val_idx]
            
            # num_colors_at_max_val represents the number of colors that are currently
            # at or above the 'current_val' and are being processed together.
            # This is effectively the count of elements from index 0 up to current_max_val_idx
            # that have been "aligned" to the current processing level.
            num_colors_at_max_val = current_max_val_idx + 1 
