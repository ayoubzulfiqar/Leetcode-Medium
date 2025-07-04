class Solution:
    def entityParser(self, text: str) -> str:
        entities = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }
        
        result = []
        i = 0
        n = len(text)
        
        while i < n:
            if text[i] == '&':
                j = i + 1
                while j < n and text[j] != ';':
                    j += 1
                
                if j < n and text[j] == ';':
                    entity_str = text[i : j + 1]
                    if entity_str in entities:
                        result.append(entities[entity_str])
                        i = j + 1
                    else:
                        result.append(text[i])
                        i += 1
                else:
                    result.append(text[i])
                    i += 1
            else:
                result.append(text[i])
                i += 1
                
        return "".join(result)