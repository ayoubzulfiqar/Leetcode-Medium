import collections

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count1 = collections.Counter(word1)
        count2 = collections.Counter(word2)

        # Condition 1: Both strings must contain the exact same set of unique characters.
        # If a character exists in word1 but not in word2 (or vice versa),
        # it's impossible to make them close. Operation 2 only swaps existing characters,
        # it doesn't introduce new character types.
        if set(count1.keys()) != set(count2.keys()):
            return False

        # Condition 2: The multiset of character frequencies must be the same.
        # Operation 1 (swapping characters) doesn't change character counts.
        # Operation 2 (transforming char_A <-> char_B) effectively reassigns counts
        # to different characters, but the set of *values* of the counts remains the same.
        # For example, if word1 has counts {a:3, b:2, c:1} and word2 has {x:3, y:2, z:1},
        # we can map a->x, b->y, c->z. The sorted list of counts [1,2,3] is identical.
        if sorted(count1.values()) != sorted(count2.values()):
            return False

        return True