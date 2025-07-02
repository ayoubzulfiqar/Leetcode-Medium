import re

def bold_words(text: str) -> str:
    """
    Bolds all sequences of alphanumeric characters within a string by wrapping them
    with <b> and </b> HTML tags. Non-alphanumeric characters (like spaces,
    punctuation) are preserved as they are.

    Args:
        text: The input string.

    Returns:
        The string with identified words bolded.
    """
    # Use re.sub to find all sequences of alphanumeric characters (words)
    # and replace them with their bolded versions.
    # The pattern r'[a-zA-Z0-9]+' matches one or more letters or digits.
    # The lambda function m: f"<b>{m.group(0)}</b>" takes the matched word
    # and formats it with bold tags.
    return re.sub(r'[a-zA-Z0-9]+', lambda m: f"<b>{m.group(0)}</b>", text)

if __name__ == '__main__':
    # Example usage (this block will not be executed if imported as a module)
    # but demonstrates the function's behavior.
    print(bold_words("Hello world"))
    print(bold_words("Hello, world! How are you?"))
    print(bold_words("This is a test with numbers 123 and symbols @#$."))
    print(bold_words(""))
    print(bold_words("   "))
    print(bold_words("OnlyOneWord"))
    print(bold_words("Word-with-hyphen")) # Hyphen is not alphanumeric, so "Word" and "with" and "hyphen" are separate.
    print(bold_words("Word_with_underscore")) # Underscore is not alphanumeric by default in [a-zA-Z0-9]+, so "Word", "with", "underscore" are separate.
                                            # If underscore should be part of a word, use r'\w+' instead.
                                            # The problem description is minimal, so [a-zA-Z0-9]+ is a safe interpretation.