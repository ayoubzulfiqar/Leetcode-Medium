class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        VOWELS = {'a', 'e', 'i', 'o', 'u'}

        # Helper function to devowel a word (replace vowels with '*')
        # Assumes input word is already lowercase.
        def _devowel(word: str) -> str:
            res = []
            for char in word:
                if char in VOWELS:
                    res.append('*')
                else:
                    res.append(char)
            return "".join(res)

        # Preprocessing the wordlist for efficient lookups based on precedence rules
        exact_matches = set(wordlist)

        # Stores lowercase word -> original word (first encountered)
        case_insensitive_matches = {}

        # Stores devowelized lowercase word -> original word (first encountered)
        vowel_error_matches = {}

        for word in wordlist:
            lower_word = word.lower()

            # For capitalization match: store the first original word for its lowercase form
            if lower_word not in case_insensitive_matches:
                case_insensitive_matches[lower_word] = word

            # For vowel error match: store the first original word for its devowelized lowercase form
            devowelized_lower_word = _devowel(lower_word)
            if devowelized_lower_word not in vowel_error_matches:
                vowel_error_matches[devowelized_lower_word] = word

        # Process queries
        results = []
        for query in queries:
            # Precedence Rule 1: Exact Match (case-sensitive)
            if query in exact_matches:
                results.append(query)
                continue

            lower_query = query.lower()

            # Precedence Rule 2: Capitalization Match (case-insensitive)
            if lower_query in case_insensitive_matches:
                results.append(case_insensitive_matches[lower_query])
                continue

            # Precedence Rule 3: Vowel Error Match (case-insensitive, vowels replaced)
            devowelized_lower_query = _devowel(lower_query)
            if devowelized_lower_query in vowel_error_matches:
                results.append(vowel_error_matches[devowelized_lower_query])
                continue

            # Precedence Rule 4: No Match
            results.append("")

        return results