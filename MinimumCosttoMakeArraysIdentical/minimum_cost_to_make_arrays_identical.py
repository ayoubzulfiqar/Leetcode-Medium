class Solution:
    def minCost(self, arr: list[int], brr: list[int], k: int) -> int:
        n = len(arr)

        cost_no_rearrangement = 0
        for i in range(n):
            cost_no_rearrangement += abs(arr[i] - brr[i])

        sorted_arr = sorted(arr)
        sorted_brr = sorted(brr)

        cost_with_rearrangement = k
        for i in range(n):
            cost_with_rearrangement += abs(sorted_arr[i] - sorted_brr[i])

        return min(cost_no_rearrangement, cost_with_rearrangement)