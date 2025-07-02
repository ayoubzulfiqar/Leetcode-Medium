class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i

        result = []
        start = 0
        current_max_reach = 0

        for i, char in enumerate(s):
            current_max_reach = max(current_max_reach, last_occurrence[char])

            if i == current_max_reach:
                result.append(i - start + 1)
                start = i + 1

        return result