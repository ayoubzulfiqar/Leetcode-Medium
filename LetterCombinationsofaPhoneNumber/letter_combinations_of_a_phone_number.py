class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if not digits:
            return []

        combinations = [""]

        for digit in digits:
            letters = phone_map[digit]
            new_combinations = []
            for combo in combinations:
                for letter in letters:
                    new_combinations.append(combo + letter)
            combinations = new_combinations
            
        return combinations