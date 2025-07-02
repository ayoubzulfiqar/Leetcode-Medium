class Solution:
    def addBoldTag(self, s: str, words: list[str]) -> str:
        n = len(s)
        bold = [False] * n

        # Step 1: Mark all characters that should be bold
        for word in words:
            start_idx = 0
            while True:
                idx = s.find(word, start_idx)
                if idx == -1:
                    break
                # Mark characters from idx to idx + len(word) - 1 as True
                for i in range(idx, idx + len(word)):
                    bold[i] = True
                # Move start_idx to find next occurrence.
                # Increment by 1 to handle overlapping matches correctly.
                start_idx = idx + 1 

        # Step 2: Construct the result string
        result = []
        i = 0
        while i < n:
            if bold[i]:
                result.append("<b>")
                # Find the end of the current bold segment
                j = i
                while j < n and bold[j]:
                    result.append(s[j])
                    j += 1
                result.append("</b>")
                i = j # Move i to the character after the bold segment
            else:
                result.append(s[i])
                i += 1
        
        return "".join(result)