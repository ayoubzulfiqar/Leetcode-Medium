class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge_map = {key: value for key, value in knowledge}
        
        result = []
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                # Found an opening bracket, extract the key
                i += 1 # Move past '('
                key_start = i
                while i < n and s[i] != ')':
                    i += 1
                
                key = s[key_start:i]
                
                # Look up the key
                value = knowledge_map.get(key, '?')
                result.append(value)
                
                i += 1 # Move past ')'
            else:
                # Not a bracket, just append the character
                result.append(s[i])
                i += 1
                
        return "".join(result)