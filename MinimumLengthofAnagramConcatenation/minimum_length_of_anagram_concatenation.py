class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)

        def get_counts(sub: str):
            counts = [0] * 26
            for char_code in map(ord, sub):
                counts[char_code - ord('a')] += 1
            return counts

        for k in range(1, n + 1):
            if n % k == 0:
                m = n // k

                target_counts = get_counts(s[0:k])

                is_valid_k = True
                for j in range(1, m):
                    current_block = s[j * k : (j + 1) * k]
                    current_counts = get_counts(current_block)

                    if current_counts != target_counts:
                        is_valid_k = False
                        break
                
                if is_valid_k:
                    return k