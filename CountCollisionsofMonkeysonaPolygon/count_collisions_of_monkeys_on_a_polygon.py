class Solution:
    def collisions(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Total number of possible movement combinations for n monkeys.
        # Each monkey has 2 choices: move clockwise or move anti-clockwise.
        # So, the total number of ways is 2 raised to the power of n.
        total_ways = pow(2, n, MOD)
        
        # We need to find the number of ways where at least one collision happens.
        # It's often easier to count the complement: ways where NO collision happens.
        
        # A collision does not happen if:
        # 1. No two monkeys end up on the same vertex.
        # 2. No two monkeys intersect on an edge during movement.
        
        # Consider the scenarios where no collision occurs:
        # Scenario 1: All monkeys move in the clockwise direction.
        #   Each monkey moves to its next vertex in clockwise order.
        #   Their relative order is preserved, so they will occupy distinct vertices, and no two will cross paths.
        #   This is 1 way.
        # Scenario 2: All monkeys move in the anti-clockwise direction.
        #   Similarly, each monkey moves to its next vertex in anti-clockwise order.
        #   Their relative order is preserved, so they will occupy distinct vertices, and no two will cross paths.
        #   This is 1 way.
        
        # Are there any other ways to avoid a collision?
        # Suppose there is a mix of clockwise and anti-clockwise movements.
        # If there's a mix, then somewhere along the polygon (circularly), there must be:
        #   a) A monkey moving clockwise followed by its clockwise neighbor moving anti-clockwise.
        #      Example: Monkey at vertex `i` moves to `(i+1)%n`, and monkey at `(i+1)%n` moves to `i`.
        #      These two monkeys will traverse the edge `(i, (i+1)%n)` in opposite directions, resulting in an edge collision.
        #   b) A monkey moving anti-clockwise followed by its clockwise neighbor moving clockwise.
        #      Example: Monkey at vertex `i` moves to `(i-1)%n`, and monkey at `(i+1)%n` moves to `(i+2)%n`.
        #      This specific configuration does not cause an immediate edge collision on `(i, (i+1)%n)`.
        
        # However, if a configuration is not purely all clockwise or purely all anti-clockwise,
        # it must contain at least one clockwise movement and at least one anti-clockwise movement.
        # Due to the circular nature of the polygon, this implies that there must exist at least one instance
        # where a monkey moving clockwise is immediately followed (clockwise) by a monkey moving anti-clockwise.
        # (If this were not true, then if you find a clockwise moving monkey, all subsequent monkeys in clockwise order must also be clockwise, leading to an all-clockwise configuration. Similarly for anti-clockwise.)
        # As established in case (a), such a configuration leads to an edge collision.
        
        # Therefore, there are exactly 2 ways in which no collision occurs.
        ways_no_collision = 2
        
        # The number of ways where at least one collision happens is the total ways minus the ways with no collision.
        # Since n >= 3, 2^n will always be greater than 2, so (total_ways - ways_no_collision) will be non-negative.
        # We add MOD before taking the final modulo to ensure the result is positive, which is good practice
        # for modular arithmetic, though not strictly necessary here because 2^n - 2 will always be >= 6.
        collisions_ways = (total_ways - ways_no_collision + MOD) % MOD
        
        return collisions_ways