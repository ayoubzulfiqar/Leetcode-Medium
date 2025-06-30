from collections import defaultdict

class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for s in strings:
            if len(s) == 1:
                # All single-character strings belong to the same shifted group.
                # An empty tuple serves as a unique key for this group.
                key = ()
            else:
                # For strings with multiple characters, calculate the differences
                # between consecutive character ASCII values, modulo 26 to handle wrap-around.
                key_parts = []
                for i in range(len(s) - 1):
                    diff = (ord(s[i+1]) - ord(s[i]) + 26) % 26
                    key_parts.append(diff)
                # Use a tuple of differences as the key for the hash map.
                key = tuple(key_parts)
            
            groups[key].append(s)
        
        # Convert the dictionary values (lists of grouped strings) to a list.
        return list(groups.values())