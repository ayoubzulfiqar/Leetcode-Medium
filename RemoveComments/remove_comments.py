class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        result = []
        current_output_line_buffer = []
        in_block_comment = False

        for line in source:
            i = 0
            while i < len(line):
                if in_block_comment:
                    if i + 1 < len(line) and line[i] == '*' and line[i+1] == '/':
                        in_block_comment = False
                        i += 2
                    else:
                        i += 1
                else:  # Not in a block comment
                    if i + 1 < len(line) and line[i] == '/' and line[i+1] == '/':
                        # Line comment found, ignore the rest of the current line
                        break  # Exit inner while loop, move to next line in source
                    elif i + 1 < len(line) and line[i] == '/' and line[i+1] == '*':
                        # Block comment start found
                        in_block_comment = True
                        i += 2
                    else:
                        # Regular code character
                        current_output_line_buffer.append(line[i])
                        i += 1
            
            # After processing a physical line
            if not in_block_comment:
                if current_output_line_buffer:  # If the buffer is not empty
                    result.append("".join(current_output_line_buffer))
                current_output_line_buffer = []  # Reset buffer for the next logical line

        return result

```python
class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        result = []
        current_output_line_buffer = []
        in_block_comment = False

        for line in source:
            i = 0
            while i < len(line):
                if in_block_comment:
                    if i + 1 < len(line) and line[i] == '*' and line[i+1] == '/':
                        in_block_comment = False
                        i += 2
                    else:
                        i += 1
                else:  # Not in a block comment
                    if i + 1 < len(line) and line[i] == '/' and line[i+1] == '/':
                        # Line comment found, ignore the rest of the current line
                        break  # Exit inner while loop, move to next line in source
                    elif i + 1 < len(line) and line[i] == '/' and line[i+1] == '*':
                        # Block comment start found
                        in_block_comment = True
                        i += 2
                    else:
                        # Regular code character
                        current_output_line_buffer.append(line[i])
                        i += 1
            
            # After processing a physical line
            if not in_block_comment:
                if current_output_line_buffer:  # If the buffer is not empty
                    result.append("".join(current_output_line_buffer))
                current_output_line_buffer = []  # Reset buffer for the next logical line

        return result
```