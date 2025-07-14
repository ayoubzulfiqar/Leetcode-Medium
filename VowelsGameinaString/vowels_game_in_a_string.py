class Solution:
    def vowelsGame(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = 0
        for char in s:
            if char in vowels:
                vowel_count += 1
        
        # Analyze the game based on the total number of vowels.
        # Let V be the total count of vowels in the string s.

        # Case 1: V is odd.
        # Alice's turn. She needs to remove a non-empty substring with an odd number of vowels.
        # Alice can choose to remove the entire string s. The string s contains V vowels, which is odd.
        # After Alice removes s, the string becomes empty.
        # Bob's turn. He needs to remove a non-empty substring. Since the string is empty, Bob cannot make a move.
        # Therefore, if V is odd, Alice wins by removing the entire string on her first move.

        # Case 2: V is even.
        # Alice's turn. She needs to remove a non-empty substring with an odd number of vowels.
        #   Subcase 2.1: V = 0.
        #   If there are no vowels in the string, any non-empty substring will also contain 0 vowels (an even number).
        #   Alice requires a substring with an odd number of vowels. She cannot find such a substring.
        #   Therefore, if V = 0, Alice cannot make a move and loses immediately.

        #   Subcase 2.2: V > 0 (i.e., V is even and positive).
        #   Since V > 0, there is at least one vowel in the string.
        #   Alice can choose to remove any single vowel character as her substring (e.g., if 'a' is at index i, remove s[i:i+1]).
        #   This substring contains 1 vowel, which is an odd number. So Alice can always make a valid move.
        #   After Alice removes a substring with 1 vowel, the remaining string will have V - 1 vowels.
        #   Since V was even, V - 1 will be odd.
        #   Now it's Bob's turn. The string has an odd number of vowels (let's call this V_rem_odd).
        #   Bob needs to remove a non-empty substring with an even number of vowels.
        #     If V_rem_odd = 1:
        #     The string contains only one vowel. The only non-empty substring is this single vowel, which has 1 vowel (odd).
        #     Bob needs an even number of vowels but can only find an odd number. Bob cannot make a move and loses. Alice wins.
        #     If V_rem_odd > 1 (and V_rem_odd is odd, so V_rem_odd >= 3):
        #     Bob can always make a valid move:
        #       - If there is at least one consonant in the string: Bob can remove a single consonant. This substring has 0 vowels (even). Valid move.
        #       - If the string consists only of vowels (and V_rem_odd >= 3): Bob can remove any two adjacent vowels. This substring has 2 vowels (even). Valid move.
        #     So, Bob can always make a move if V_rem_odd > 1.
        #     After Bob removes a substring with an even number of vowels (say, k_even vowels), the remaining string will have V_rem_odd - k_even vowels.
        #     Since V_rem_odd is odd and k_even is even, V_rem_odd - k_even will be odd.
        #     Thus, after Bob's move, the string will still have an odd number of vowels.
        #   The game continues with the number of vowels decreasing. The number of vowels will always be odd when it's a player's turn, until it reaches 1.
        #   When the number of vowels becomes 1:
        #     - If it's Alice's turn: She removes the single vowel (1 vowel, odd). The string becomes empty. Bob loses. Alice wins.
        #     - If it's Bob's turn: He needs an even number of vowels, but only 1 vowel is available. Bob cannot make a move. Bob loses. Alice wins.
        #   Therefore, if V is even and positive, Alice always wins.

        # Combining all cases:
        # Alice wins if V is odd.
        # Alice wins if V is even and V > 0.
        # Alice loses if V = 0.
        # This simplifies to: Alice wins if and only if the total number of vowels is greater than 0.

        return vowel_count > 0