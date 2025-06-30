class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_revisions = version1.split('.')
        v2_revisions = version2.split('.')

        len1 = len(v1_revisions)
        len2 = len(v2_revisions)

        # Determine the maximum number of revisions to check
        # This ensures we iterate through all significant parts of both versions
        max_len = max(len1, len2)

        for i in range(max_len):
            # Get the revision for version1 at the current index
            # If the index is out of bounds for version1, treat the revision as 0
            rev1 = 0
            if i < len1:
                rev1 = int(v1_revisions[i])

            # Get the revision for version2 at the current index
            # If the index is out of bounds for version2, treat the revision as 0
            rev2 = 0
            if i < len2:
                rev2 = int(v2_revisions[i])

            # Compare the integer values of the current revisions
            if rev1 < rev2:
                return -1  # version1 is smaller
            elif rev1 > rev2:
                return 1   # version1 is larger
            # If rev1 == rev2, continue to the next revision

        # If the loop completes, it means all corresponding revisions were equal
        # and any trailing missing revisions were treated as 0 and also equal.
        # Therefore, the versions are identical.
        return 0