import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_groups = collections.defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            anagram_groups[sorted_s].append(s)

        return list(anagram_groups.values())