import collections

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        even_counts = collections.Counter()
        odd_counts = collections.Counter()

        for i in range(n):
            if i % 2 == 0:
                even_counts[nums[i]] += 1
            else:
                odd_counts[nums[i]] += 1

        n_even = (n + 1) // 2
        n_odd = n // 2

        even_items = even_counts.most_common(2)
        e1_val, e1_freq = even_items[0] if even_items else (0, 0)
        e2_val, e2_freq = even_items[1] if len(even_items) > 1 else (0, 0)

        odd_items = odd_counts.most_common(2)
        o1_val, o1_freq = odd_items[0] if odd_items else (0, 0)
        o2_val, o2_freq = odd_items[1] if len(odd_items) > 1 else (0, 0)

        if e1_val != o1_val:
            operations = (n_even - e1_freq) + (n_odd - o1_freq)
        else:
            ops1 = (n_even - e1_freq) + (n_odd - o2_freq)
            ops2 = (n_even - e2_freq) + (n_odd - o1_freq)
            operations = min(ops1, ops2)
        
        return operations