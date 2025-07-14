import collections

class Solution:
    def mostCommonResponse(self, responses: list[list[str]]) -> str:
        all_response_counts = collections.Counter()

        for day_responses in responses:
            unique_day_responses = set(day_responses)
            for response in unique_day_responses:
                all_response_counts[response] += 1

        most_common_response = ""
        max_freq = -1

        for response, freq in all_response_counts.items():
            if freq > max_freq:
                max_freq = freq
                most_common_response = response
            elif freq == max_freq:
                if response < most_common_response:
                    most_common_response = response
        
        return most_common_response