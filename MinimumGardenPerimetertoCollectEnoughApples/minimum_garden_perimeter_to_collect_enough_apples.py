class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        # The problem asks for the minimum perimeter of an axis-aligned square plot
        # centered at (0, 0) such that it contains at least neededApples.
        # A square plot centered at (0, 0) with a side length of 2k (meaning it extends
        # from -k to k on both the x and y axes) covers all integer coordinates (i, j)
        # such that max(|i|, |j|) <= k.
        # The perimeter of such a square is 4 * (2k) = 8k.

        # We need to find a formula for the total number of apples within such a square.
        # The number of apples at coordinate (i, j) is |i| + |j|.
        # The total apples for a square defined by max(|i|, |j|) <= k is:
        # Sum_{i=-k to k} Sum_{j=-k to k} (|i| + |j|)
        # This sum can be split into two parts:
        # Sum_{i=-k to k} Sum_{j=-k to k} |i|  +  Sum_{i=-k to k} Sum_{j=-k to k} |j|
        #
        # For the first part, Sum_{j=-k to k} |i| = (2k + 1) * |i| (since |i| is constant for inner sum)
        # So, Sum_{i=-k to k} (2k + 1) * |i| = (2k + 1) * Sum_{i=-k to k} |i|
        #
        # The sum Sum_{i=-k to k} |i| can be calculated as:
        # |0| + 2 * Sum_{i=1 to k} i = 0 + 2 * (k * (k + 1) / 2) = k * (k + 1)
        #
        # Substituting this back:
        # The first part is (2k + 1) * k * (k + 1)
        # The second part (Sum_{i=-k to k} Sum_{j=-k to k} |j|) is identical by symmetry:
        # (2k + 1) * k * (k + 1)
        #
        # So, the total number of apples (let's call it `apples_for_k`) is:
        # `apples_for_k = (2k + 1) * k * (k + 1) + (2k + 1) * k * (k + 1)`
        # `apples_for_k = 2 * k * (k + 1) * (2k + 1)`

        # We need to find the smallest integer `k` such that `apples_for_k >= neededApples`.
        # Since `apples_for_k` is a monotonically increasing function of `k` (for k >= 0),
        # we can use binary search to find the minimum `k`.

        # The maximum value of `neededApples` is 10^15.
        # `2k(k+1)(2k+1)` is approximately `4k^3`.
        # So, `4k^3 >= 10^15` implies `k^3 >= 0.25 * 10^15`.
        # `k >= (0.25 * 10^15)^(1/3) = (250 * 10^12)^(1/3) = (250)^(1/3) * 10^4`.
        # Since 6^3 = 216 and 7^3 = 343, (250)^(1/3) is between 6 and 7 (approx 6.3).
        # So, `k` will be around `6.3 * 10^4 = 63000`.
        # A safe upper bound for binary search can be `2 * 10^5`.

        low = 0
        high = 2 * 10**5  # A sufficiently large upper bound for k
        ans_k = high      # Initialize with a value that is guaranteed to satisfy the condition

        while low <= high:
            mid = low + (high - low) // 2
            
            # Calculate the number of apples for the current `mid` value of `k`.
            # Python's integers handle arbitrary precision, so overflow is not an issue.
            current_apples = 2 * mid * (mid + 1) * (2 * mid + 1)
            
            if current_apples >= neededApples:
                # If enough apples are collected, this `mid` is a possible answer.
                # Try to find a smaller `k` by searching in the lower half.
                ans_k = mid
                high = mid - 1
            else:
                # Not enough apples, need a larger `k`.
                # Search in the upper half.
                low = mid + 1
                
        # The minimum perimeter is 8 times the minimum `k` found.
        return 8 * ans_k