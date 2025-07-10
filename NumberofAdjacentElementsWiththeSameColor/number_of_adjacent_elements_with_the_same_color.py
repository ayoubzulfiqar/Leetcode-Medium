class Solution:
    def colorTheArray(self, n: int, queries: list[list[int]]) -> list[int]:
        colors = [0] * n
        current_same_color_pairs_count = 0
        answer = []

        for index, new_color in queries:
            old_color = colors[index]

            # Check left neighbor
            if index > 0:
                # If old_color formed a pair with left neighbor, decrement count
                if colors[index - 1] == old_color and old_color != 0:
                    current_same_color_pairs_count -= 1
                # If new_color forms a pair with left neighbor, increment count
                if colors[index - 1] == new_color and new_color != 0:
                    current_same_color_pairs_count += 1
            
            # Check right neighbor
            if index < n - 1:
                # If old_color formed a pair with right neighbor, decrement count
                if colors[index + 1] == old_color and old_color != 0:
                    current_same_color_pairs_count -= 1
                # If new_color forms a pair with right neighbor, increment count
                if colors[index + 1] == new_color and new_color != 0:
                    current_same_color_pairs_count += 1
            
            # Update the color at the current index
            colors[index] = new_color
            
            # Add the current count to the answer list
            answer.append(current_same_color_pairs_count)
            
        return answer