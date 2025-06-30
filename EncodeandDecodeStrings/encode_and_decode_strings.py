class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if not strs:
            return ""

        encoded_string_parts = []
        for s in strs:
            encoded_string_parts.append(str(len(s)))
            encoded_string_parts.append("#")  # Delimiter
            encoded_string_parts.append(s)
        return "".join(encoded_string_parts)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        if not s:
            return []

        decoded_strs = []
        i = 0
        n = len(s)

        while i < n:
            # Find the delimiter '#'
            j = i
            while j < n and s[j] != '#':
                j += 1

            # Extract the length string (e.g., "5" from "5#hello")
            length_str = s[i:j]
            length = int(length_str)

            # The actual string starts after the delimiter
            # and has the extracted 'length'
            start_of_string = j + 1
            end_of_string = start_of_string + length
            
            decoded_strs.append(s[start_of_string:end_of_string])

            # Move pointer to the start of the next length prefix
            i = end_of_string
            
        return decoded_strs