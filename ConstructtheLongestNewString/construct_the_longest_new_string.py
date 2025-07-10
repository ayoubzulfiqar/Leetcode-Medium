class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # To maximize the length while avoiding "AAA" or "BBB",
        # the "AA" and "BB" strings must be arranged in an alternating pattern.
        # For example, "AABBAABB..." or "BBAABBAA...".

        # We can always use `min(x, y)` pairs of "AA" and "BB" strings.
        # This accounts for `2 * min(x, y)` blocks (e.g., min(x,y) "AA"s and min(x,y) "BB"s).
        # If `x` and `y` are not equal, we will have an excess of either "AA" or "BB" strings.
        # We can use one additional block of the more frequent type.
        # For example, if x=3, y=2, we can use 2 "AA"s and 2 "BB"s (e.g., "AABBAABB"),
        # and then one more "AA" (e.g., "AABBAABBAA").
        # So, if x != y, we can use `min(x, y) + min(x, y) + 1` blocks.
        # If x == y, we can use `min(x, y) + min(x, y)` blocks.

        # Calculate the number of "AA" and "BB" blocks that can be used.
        num_aa_bb_blocks = 2 * min(x, y)
        if x != y:
            num_aa_bb_blocks += 1
        
        # Each "AA" or "BB" block contributes 2 to the total length.
        length_from_aa_bb = num_aa_bb_blocks * 2
        
        # The "AB" strings can be placed anywhere without creating "AAA" or "BBB" substrings,
        # as they inherently break sequences of 'A's or 'B's.
        # Therefore, we can always use all `z` "AB" strings.
        # Each "AB" block contributes 2 to the total length.
        length_from_ab = z * 2
        
        # The total maximum length is the sum of lengths from "AA"/"BB" and "AB" strings.
        return length_from_aa_bb + length_from_ab