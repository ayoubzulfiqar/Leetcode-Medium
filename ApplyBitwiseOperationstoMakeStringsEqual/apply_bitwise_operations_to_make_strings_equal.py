class Solution:
    def canMakeStringsEqual(self, s: str, target: str) -> bool:
        count_s_ones = s.count('1')
        count_target_ones = target.count('1')

        if count_s_ones == 0:
            # If s has no '1's, it can only stay "00...0".
            # Thus, target must also be "00...0".
            return count_target_ones == 0
        else: # count_s_ones >= 1
            # If s has at least one '1':
            # 1. We can turn any '0' into a '1' by pairing it with an existing '1'
            #    (e.g., (0,1) -> (1,1)). This allows us to reach a state of all '1's.
            # 2. If there are at least two '1's (which can be achieved if needed from step 1),
            #    we can turn a '1' into a '0' by pairing it with another '1'
            #    (e.g., (1,1) -> (1,0)). This allows us to reduce the number of '1's down to one '1'.
            # Combining these capabilities, if s starts with at least one '1', we can reach
            # any string that has at least one '1'.
            # Therefore, target must also have at least one '1'.
            return count_target_ones >= 1