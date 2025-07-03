class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = [0] * len(seq)
        depth = 0
        for i, char in enumerate(seq):
            if char == '(':
                ans[i] = depth % 2
                depth += 1
            else:  # char == ')'
                depth -= 1
                ans[i] = depth % 2
        return ans