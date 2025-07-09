class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(' ')
        result_words = []

        for word in words:
            # Check if the word represents a price
            # It must start with '$', be longer than just '$',
            # and all characters after '$' must be digits.
            if word.startswith('$') and len(word) > 1 and word[1:].isdigit():
                price_str = word[1:]
                original_price = float(price_str)
                
                # Calculate the discounted price
                # discount is an integer percentage (e.g., 50 for 50%)
                # So, (100 - discount) / 100.0 gives the multiplier
                discount_factor = (100 - discount) / 100.0
                discounted_price = original_price * discount_factor
                
                # Format the discounted price to exactly two decimal places
                # and prepend '$'
                result_words.append(f"${discounted_price:.2f}")
            else:
                # If it's not a price word, keep it as is
                result_words.append(word)
        
        # Join the processed words back into a single sentence
        return ' '.join(result_words)