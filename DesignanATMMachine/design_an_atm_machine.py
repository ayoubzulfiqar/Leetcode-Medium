class ATM:
    def __init__(self):
        # Stores the count of banknotes in the order: 20, 50, 100, 200, 500
        self.banknotes = [0, 0, 0, 0, 0]
        # Denominations in descending order, paired with their corresponding index
        # in the self.banknotes list (for 20, 50, 100, 200, 500)
        self.denominations_desc = [(500, 4), (200, 3), (100, 2), (50, 1), (20, 0)]

    def deposit(self, banknotesCount: list[int]) -> None:
        for i in range(5):
            self.banknotes[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> list[int]:
        # Temporary list to store banknotes to be withdrawn during simulation
        temp_banknotes_taken = [0, 0, 0, 0, 0]
        
        # Create a copy of current ATM banknotes to simulate withdrawal without
        # modifying the actual state until the withdrawal is confirmed successful.
        current_atm_banknotes_copy = list(self.banknotes)
        
        remaining_amount = amount
        
        # Iterate from largest denomination to smallest, prioritizing larger values
        for value, idx in self.denominations_desc:
            if remaining_amount == 0:
                break # If the amount is already covered, no need to process smaller denominations
            
            # Calculate how many banknotes of this denomination can be taken
            # It's the minimum of what's needed (remaining_amount // value)
            # and what's available in the ATM (current_atm_banknotes_copy[idx]).
            num_to_take = min(remaining_amount // value, current_atm_banknotes_copy[idx])
            
            # Record the number of banknotes taken for this denomination
            temp_banknotes_taken[idx] += num_to_take
            
            # Update the remaining amount to be withdrawn
            remaining_amount -= num_to_take * value
            
            # Update the count in the simulated ATM copy
            current_atm_banknotes_copy[idx] -= num_to_take

        if remaining_amount == 0:
            # If remaining_amount is 0, the withdrawal is successful.
            # Update the actual ATM banknotes.
            for i in range(5):
                self.banknotes[i] -= temp_banknotes_taken[i]
            return temp_banknotes_taken
        else:
            # If remaining_amount is not 0, the withdrawal is not possible
            # with the given greedy strategy. Return [-1] and do not modify
            # the ATM's banknotes.
            return [-1]