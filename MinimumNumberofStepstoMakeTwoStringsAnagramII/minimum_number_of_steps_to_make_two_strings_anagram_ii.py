import collections

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = collections.Counter(s)
        count_t = collections.Counter(t)

        total_steps = 0

        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            
            freq_s = count_s[char]
            freq_t = count_t[char]

            target_freq = max(freq_s, freq_t)
            
            steps_for_s = target_freq - freq_s
            steps_for_t = target_freq - freq_t
            
            total_steps += steps_for_s + steps_for_t
            
        return total_steps