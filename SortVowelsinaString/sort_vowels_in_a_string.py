class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        extracted_vowels = []
        vowel_indices = []
        
        for i, char in enumerate(s):
            if char in vowels_set:
                extracted_vowels.append(char)
                vowel_indices.append(i)
        
        extracted_vowels.sort()
        
        result_list = list(s)
        
        for i in range(len(vowel_indices)):
            original_index = vowel_indices[i]
            sorted_vowel = extracted_vowels[i]
            result_list[original_index] = sorted_vowel
            
        return "".join(result_list)