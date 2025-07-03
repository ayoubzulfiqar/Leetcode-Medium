def encode_number(number: int, alphabet: str) -> str:
    """
    Encodes an integer into a string using a custom alphabet.

    Args:
        number: The integer to encode. Must be non-negative.
        alphabet: A string containing the unique characters to use for encoding.
                  The length of the alphabet determines the base of the encoding.

    Returns:
        A string representation of the number in the given alphabet.
    """
    if number == 0:
        return alphabet[0]

    base = len(alphabet)
    if base == 0:
        raise ValueError("Alphabet cannot be empty.")

    encoded_chars = []
    while number > 0:
        remainder = number % base
        encoded_chars.append(alphabet[remainder])
        number //= base

    return "".join(reversed(encoded_chars))

if __name__ == '__main__':
    # Example Usage:
    # Base 10 (decimal)
    alphabet_decimal = "0123456789"
    num1 = 12345
    encoded1 = encode_number(num1, alphabet_decimal)
    # print(f"Number: {num1}, Alphabet: '{alphabet_decimal}', Encoded: {encoded1}") # Expected: 12345

    # Base 62 (common for short URLs, 0-9, a-z, A-Z)
    alphabet_base62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num2 = 123456789
    encoded2 = encode_number(num2, alphabet_base62)
    # print(f"Number: {num2}, Alphabet: '{alphabet_base62}', Encoded: {encoded2}") # Expected: 15Y8X

    num3 = 0
    encoded3 = encode_number(num3, alphabet_base62)
    # print(f"Number: {num3}, Alphabet: '{alphabet_base62}', Encoded: {encoded3}") # Expected: 0

    num4 = 61
    encoded4 = encode_number(num4, alphabet_base62)
    # print(f"Number: {num4}, Alphabet: '{alphabet_base62}', Encoded: {encoded4}") # Expected: Z

    num5 = 62
    encoded5 = encode_number(num5, alphabet_base62)
    # print(f"Number: {num5}, Alphabet: '{alphabet_base62}', Encoded: {encoded5}") # Expected: 10

    # Custom alphabet (e.g., hex)
    alphabet_hex = "0123456789ABCDEF"
    num6 = 255
    encoded6 = encode_number(num6, alphabet_hex)
    # print(f"Number: {num6}, Alphabet: '{alphabet_hex}', Encoded: {encoded6}") # Expected: FF