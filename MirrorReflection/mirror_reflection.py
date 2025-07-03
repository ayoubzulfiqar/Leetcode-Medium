import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        common_divisor = math.gcd(p, q)

        # num_p_x represents the number of 'p' units the ray travels horizontally
        # in the unfolded grid before hitting a corner.
        # num_p_y represents the number of 'p' units the ray travels vertically
        # in the unfolded grid before hitting a corner.
        # These are derived from simplifying the ratio q/p.
        num_p_x = p // common_divisor
        num_p_y = q // common_divisor

        # Determine the receptor based on the parity of num_p_x and num_p_y.
        # In the unfolded grid, the ray starts at (0,0) and ends at (num_p_x * p, num_p_y * p).
        #
        # If num_p_x is odd, the ray's final x-coordinate in the original room is p (right wall).
        # If num_p_x is even, the ray's final x-coordinate in the original room is 0 (left wall).
        #
        # If num_p_y is odd, the ray's final y-coordinate in the original room is p (top wall).
        # If num_p_y is even, the ray's final y-coordinate in the original room is 0 (bottom wall).
        #
        # Receptors are located at:
        # Receptor 0: (p, 0)
        # Receptor 1: (p, p)
        # Receptor 2: (0, p)
        #
        # Note: num_p_x and num_p_y are coprime, so they cannot both be even.

        if num_p_x % 2 == 1:  # Final x-coordinate is p (right wall)
            if num_p_y % 2 == 1:  # Final y-coordinate is p (top wall)
                return 1  # Hits (p, p)
            else:  # Final y-coordinate is 0 (bottom wall)
                return 0  # Hits (p, 0)
        else:  # Final x-coordinate is 0 (left wall)
            # Since num_p_x and num_p_y are coprime, if num_p_x is even, num_p_y must be odd.
            # So, final y-coordinate must be p (top wall).
            return 2  # Hits (0, p)