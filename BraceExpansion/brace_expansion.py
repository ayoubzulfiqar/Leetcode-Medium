import itertools

class Solution:
    def braceExpansion(self, s: str) -> list[str]:
        parsed_blocks = []
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '{':
                j = s.find('}', i)
                content = s[i+1:j]
                options = sorted(content.split(','))
                parsed_blocks.append(options)
                i = j + 1
            else:
                start_literal = i
                while i < n and s[i] != '{':
                    i += 1
                literal = s[start_literal:i]
                parsed_blocks.append([literal])

        result = []
        for combination_tuple in itertools.product(*parsed_blocks):
            result.append("".join(combination_tuple))
        
        return sorted(result)