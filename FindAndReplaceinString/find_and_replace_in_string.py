```python
class Solution:
    def findReplaceString(self, s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
        replacements_map = {}
        for i in range(len(indices)):
            idx = indices[i]
            src = sources[i]
            tgt = targets[i]

            # Check if the source string actually occurs at the given index in s
            # and if it fits within the bounds of s.
            if s[idx:idx + len(src)] == src:
                replacements_map[idx] = (len(src), tgt)
        
        result_chars = []
        
        i = 0
        while i < len(s):
            # Check if there is a replacement operation starting at the current index i
            if i in replacements_map:
                source_len, target_str = replacements_map[i]
                result_chars.append(target_str)
                # Advance the pointer past the replaced source string
                i += source_len
            else:
                # No replacement at this index, so just append the original character
                result_chars.append(s[i])
                # Advance the pointer by one character
                i += 1
                
        return "".join(result_chars)

```