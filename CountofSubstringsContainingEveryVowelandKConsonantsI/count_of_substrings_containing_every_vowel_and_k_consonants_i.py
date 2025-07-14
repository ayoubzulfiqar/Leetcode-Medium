def countSubstrings(word: str, k: int) -> int:
    n = len(word)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    total_valid_substrings = 0

    for i in range(n):
        current_vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        current_consonant_count = 0
        unique_vowels_found = 0

        for j in range(i, n):
            char = word[j]

            if char in vowels:
                if current_vowel_counts[char] == 0:
                    unique_vowels_found += 1
                current_vowel_counts[char] += 1
            else:
                current_consonant_count += 1
            
            if unique_vowels_found == 5 and current_consonant_count == k:
                total_valid_substrings += 1
                
    return total_valid_substrings