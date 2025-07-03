import collections

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        max_fruits = 0
        left = 0
        fruit_counts = collections.defaultdict(int)

        for right in range(len(fruits)):
            fruit_counts[fruits[right]] += 1

            while len(fruit_counts) > 2:
                fruit_counts[fruits[left]] -= 1
                if fruit_counts[fruits[left]] == 0:
                    del fruit_counts[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits