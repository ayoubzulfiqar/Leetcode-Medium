class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()

        result = []
        left = 0
        right = len(products) - 1

        for i in range(len(searchWord)):
            char_to_match = searchWord[i]

            while left <= right and (len(products[left]) <= i or products[left][i] != char_to_match):
                left += 1

            while left <= right and (len(products[right]) <= i or products[right][i] != char_to_match):
                right -= 1

            current_suggestions = []
            for j in range(left, min(left + 3, right + 1)):
                current_suggestions.append(products[j])
            
            result.append(current_suggestions)
            
        return result