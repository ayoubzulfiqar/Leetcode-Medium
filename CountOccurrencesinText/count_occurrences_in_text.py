import re

def count_occurrences(text: str, word: str) -> int:
    """
    Counts the occurrences of a specific word in a given text, case-insensitively,
    considering whole words only.

    Args:
        text (str): The input text to search within.
        word (str): The word to count occurrences of.

    Returns:
        int: The number of times the word appears as a whole word in the text.
    """
    if not text or not word:
        return 0

    target_word = word.lower()
    
    # Use regex to find all whole words in the text.
    # \b is a word boundary, ensuring we match whole words.
    # \w matches alphanumeric characters and underscore.
    # Convert the entire text to lowercase before finding words for case-insensitivity.
    words_in_text = re.findall(r'\b\w+\b', text.lower())
    
    count = 0
    for w in words_in_text:
        if w == target_word:
            count += 1
            
    return count

# Example usage to demonstrate functionality
# These lines will execute when the script is run.
print(count_occurrences("Hello world, hello Python!", "hello"))
print(count_occurrences("This is a test. Is this good? Yes, this is.", "is"))
print(count_occurrences("Python is great. python is powerful.", "Python"))
print(count_occurrences("Apple Banana Orange", "grape"))
print(count_occurrences("", "word"))
print(count_occurrences("Some text", ""))
print(count_occurrences("Word-Word Word", "word"))
print(count_occurrences("The quick brown fox jumps over the lazy dog. The dog is very lazy.", "the"))
print(count_occurrences("One two three four five. One two three.", "one"))
print(count_occurrences("Test Test Test", "test"))
print(count_occurrences("Testing, testing, 1 2 3.", "testing"))
print(count_occurrences("Underscore_word_test", "underscore_word_test"))
print(count_occurrences("Underscore_word_test", "word"))